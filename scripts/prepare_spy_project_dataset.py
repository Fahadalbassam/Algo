"""
Build a clean SPY options project dataset: join FRED DGS3MO (risk-free proxy) by quote date.

Reads:  data/milestone/option_SPY_dataset_combined.csv
Writes: data/raw/fred_dgs3mo.csv (cached download)
         data/processed/spy_options_project_dataset.csv
"""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import pandas as pd
except ImportError as exc:  # pragma: no cover - import guard for optional dep
    print(
        "This script requires pandas. Install with: pip install pandas",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = ROOT / "data" / "milestone" / "option_SPY_dataset_combined.csv"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS3MO"
FRED_CACHE = ROOT / "data" / "raw" / "fred_dgs3mo.csv"
OUTPUT_PATH = ROOT / "data" / "processed" / "spy_options_project_dataset.csv"

FINAL_COLUMNS = [
    "quote_date",
    "expiry_date",
    "option_type",
    "S",
    "K",
    "T",
    "r",
    "sigma",
    "market_option_price",
    "bid",
    "ask",
    "open_interest",
]


def download_fred_dgs3mo(dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        FRED_URL,
        headers={"User-Agent": "AlgoProjectDatasetPrep/1.0 (research; +https://github.com)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.URLError as e:
        print(f"Failed to download FRED DGS3MO: {e}", file=sys.stderr)
        raise SystemExit(1) from e
    dest.write_bytes(data)


def load_fred_rates(cache_path: Path, refresh: bool) -> pd.DataFrame:
    if refresh or not cache_path.exists():
        print(f"Downloading FRED DGS3MO -> {cache_path}")
        download_fred_dgs3mo(cache_path)
    else:
        print(f"Using cached FRED file: {cache_path}")

    fred = pd.read_csv(cache_path)
    if "observation_date" not in fred.columns or "DGS3MO" not in fred.columns:
        print(
            "Unexpected FRED CSV columns; expected observation_date and DGS3MO.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    fred["fred_date"] = pd.to_datetime(fred["observation_date"], errors="coerce")
    fred["DGS3MO"] = pd.to_numeric(fred["DGS3MO"], errors="coerce")
    fred = fred.dropna(subset=["fred_date", "DGS3MO"])
    fred = fred.sort_values("fred_date").drop_duplicates(subset=["fred_date"], keep="last")
    fred["r"] = fred["DGS3MO"] / 100.0
    return fred[["fred_date", "r"]]


def load_options(source: Path) -> pd.DataFrame:
    opts = pd.read_csv(source)
    required = (
        "dt",
        "expr",
        "underlying",
        "strike",
        "daysToExpiration",
        "iv",
        "mark",
        "bid",
        "ask",
        "openInterest",
    )
    missing = [c for c in required if c not in opts.columns]
    if missing:
        print(f"Source CSV missing columns: {missing}", file=sys.stderr)
        raise SystemExit(1)
    return opts


def build_project_frame(opts: pd.DataFrame, fred: pd.DataFrame) -> pd.DataFrame:
    q = opts.copy()
    q["quote_date"] = pd.to_datetime(q["dt"], errors="coerce")
    q = q.dropna(subset=["quote_date"]).sort_values("quote_date")

    merged = pd.merge_asof(
        q,
        fred,
        left_on="quote_date",
        right_on="fred_date",
        direction="backward",
        allow_exact_matches=True,
    )
    merged = merged.drop(columns=["fred_date"], errors="ignore")

    out = pd.DataFrame(
        {
            "quote_date": merged["quote_date"].dt.normalize(),
            "expiry_date": pd.to_datetime(merged["expr"], errors="coerce").dt.normalize(),
            "option_type": "call",
            "S": pd.to_numeric(merged["underlying"], errors="coerce"),
            "K": pd.to_numeric(merged["strike"], errors="coerce"),
            "T": pd.to_numeric(merged["daysToExpiration"], errors="coerce") / 365.0,
            "r": merged["r"],
            "sigma": pd.to_numeric(merged["iv"], errors="coerce"),
            "market_option_price": pd.to_numeric(merged["mark"], errors="coerce"),
            "bid": pd.to_numeric(merged["bid"], errors="coerce"),
            "ask": pd.to_numeric(merged["ask"], errors="coerce"),
            "open_interest": pd.to_numeric(merged["openInterest"], errors="coerce"),
        }
    )

    valid = (
        out["quote_date"].notna()
        & out["expiry_date"].notna()
        & (out["S"] > 0)
        & (out["K"] > 0)
        & (out["T"] > 0)
        & (out["sigma"] > 0)
        & (out["market_option_price"] > 0)
        & (out["open_interest"] >= 0)
        & (out["bid"] >= 0)
        & (out["ask"] >= 0)
        & (out["r"].notna())
    )
    return out.loc[valid, FINAL_COLUMNS].reset_index(drop=True)


def print_summary(source_rows: int, out: pd.DataFrame) -> None:
    print()
    print("--- SPY project dataset summary ---")
    print(f"Input rows:  {source_rows}")
    print(f"Output rows: {len(out)}")
    if len(out) == 0:
        print("(No rows after filters; skipping date ranges.)")
    else:
        print(f"quote_date min:  {out['quote_date'].min()}")
        print(f"quote_date max:  {out['quote_date'].max()}")
        print(f"expiry_date min: {out['expiry_date'].min()}")
        print(f"expiry_date max: {out['expiry_date'].max()}")
    print("Null counts (final columns):")
    nulls = out.isna().sum()
    for col in FINAL_COLUMNS:
        print(f"  {col}: {int(nulls[col])}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Path to option_SPY_dataset_combined.csv",
    )
    p.add_argument(
        "--fred-cache",
        type=Path,
        default=FRED_CACHE,
        help="Where to store downloaded FRED CSV",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_PATH,
        help="Output processed CSV path",
    )
    p.add_argument(
        "--refresh-fred",
        action="store_true",
        help="Re-download FRED DGS3MO even if cache exists",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    if not source.is_file():
        print(f"Source file not found: {source}", file=sys.stderr)
        return 1

    opts = load_options(source)
    input_count = len(opts)

    fred = load_fred_rates(args.fred_cache.resolve(), refresh=args.refresh_fred)
    out = build_project_frame(opts, fred)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)

    print(f"Wrote: {args.output}")
    print_summary(input_count, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
