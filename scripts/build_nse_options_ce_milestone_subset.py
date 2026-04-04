from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE = ROOT / "nse_options_2024-11-03_normalized.csv"
OUTPUT_FILE = (
    ROOT
    / "data"
    / "milestone"
    / "nse_options_2024-11-03_normalized_ce_milestone_subset.csv"
)

OUTPUT_SCHEMA = [
    "source_row_id",
    "raw_ticker",
    "exchange",
    "underlying_symbol",
    "option_type",
    "expiry_date",
    "strike_price",
    "quote_date",
    "quote_time",
    "quote_datetime",
    "days_to_expiry",
    "time_to_expiry_years",
    "market_option_price",
    "volume",
    "open_interest",
    "open_interest_overflow_flag",
]


def parse_positive_float(value: str) -> bool:
    return float(value.strip()) > 0


def parse_positive_int(value: str) -> bool:
    return int(value.strip()) > 0


def row_matches_locked_filters(row: dict[str, str]) -> bool:
    return (
        row["instrument_type"] == "OPTION"
        and row["option_type"] == "CE"
        and parse_positive_float(row["time_to_expiry_years"])
        and parse_positive_int(row["open_interest"])
        and parse_positive_float(row["close_price"])
        and parse_positive_float(row["strike_price"])
    )


def transform_row(source_row_id: int, row: dict[str, str]) -> dict[str, str]:
    return {
        "source_row_id": str(source_row_id),
        "raw_ticker": row["raw_ticker"],
        "exchange": row["exchange"],
        "underlying_symbol": row["underlying_symbol"],
        "option_type": row["option_type"],
        "expiry_date": row["expiry_date"],
        "strike_price": row["strike_price"],
        "quote_date": row["quote_date"],
        "quote_time": row["quote_time"],
        "quote_datetime": row["quote_datetime"],
        "days_to_expiry": row["days_to_expiry"],
        "time_to_expiry_years": row["time_to_expiry_years"],
        "market_option_price": row["close_price"],
        "volume": row["volume"],
        "open_interest": row["open_interest"],
        "open_interest_overflow_flag": row["open_interest_overflow_flag"],
    }


def main() -> int:
    if not SOURCE_FILE.exists():
        print(f"Source file not found: {SOURCE_FILE}", file=sys.stderr)
        return 1

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    before_count = 0
    after_count = 0

    with SOURCE_FILE.open("r", newline="", encoding="utf-8-sig") as source_handle:
        reader = csv.DictReader(source_handle)

        with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as output_handle:
            writer = csv.DictWriter(
                output_handle,
                fieldnames=OUTPUT_SCHEMA,
                lineterminator="\n",
            )
            writer.writeheader()

            for source_row_id, row in enumerate(reader, start=1):
                before_count += 1
                if not row_matches_locked_filters(row):
                    continue

                writer.writerow(transform_row(source_row_id, row))
                after_count += 1

    print(f"Source file: {SOURCE_FILE.name}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Rows before filtering: {before_count}")
    print(f"Rows after filtering: {after_count}")
    print(f"Output schema: {','.join(OUTPUT_SCHEMA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
