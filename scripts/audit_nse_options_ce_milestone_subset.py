from __future__ import annotations

import csv
import sys
from collections import Counter
from datetime import datetime
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
DATE_FORMAT = "%m/%d/%Y"
TIME_TO_EXPIRY_TOLERANCE = 1e-6


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


def build_expected_output_row(
    source_row_id: int,
    source_row: dict[str, str],
) -> dict[str, str]:
    return {
        "source_row_id": str(source_row_id),
        "raw_ticker": source_row["raw_ticker"],
        "exchange": source_row["exchange"],
        "underlying_symbol": source_row["underlying_symbol"],
        "option_type": source_row["option_type"],
        "expiry_date": source_row["expiry_date"],
        "strike_price": source_row["strike_price"],
        "quote_date": source_row["quote_date"],
        "quote_time": source_row["quote_time"],
        "quote_datetime": source_row["quote_datetime"],
        "days_to_expiry": source_row["days_to_expiry"],
        "time_to_expiry_years": source_row["time_to_expiry_years"],
        "market_option_price": source_row["close_price"],
        "volume": source_row["volume"],
        "open_interest": source_row["open_interest"],
        "open_interest_overflow_flag": source_row["open_interest_overflow_flag"],
    }


def report_error(errors: list[str], message: str) -> None:
    if len(errors) < 25:
        errors.append(message)


def validate_output_row(
    row_number: int,
    row: dict[str, str],
    seen_source_row_ids: set[str],
    overflow_counts: Counter[str],
    errors: list[str],
) -> None:
    for field in OUTPUT_SCHEMA:
        value = row.get(field, "")
        if value is None or value.strip() == "":
            report_error(errors, f"Row {row_number}: blank required field '{field}'.")

    source_row_id = row.get("source_row_id", "").strip()
    if source_row_id in seen_source_row_ids:
        report_error(errors, f"Row {row_number}: duplicate source_row_id '{source_row_id}'.")
    else:
        seen_source_row_ids.add(source_row_id)

    try:
        if int(source_row_id) <= 0:
            report_error(errors, f"Row {row_number}: source_row_id must be > 0.")
    except ValueError:
        report_error(errors, f"Row {row_number}: source_row_id is not an integer.")

    if row.get("option_type") != "CE":
        report_error(errors, f"Row {row_number}: option_type is not CE.")

    try:
        strike_price = float(row["strike_price"])
        if strike_price <= 0:
            report_error(errors, f"Row {row_number}: strike_price must be > 0.")
    except ValueError:
        report_error(errors, f"Row {row_number}: strike_price is not numeric.")

    try:
        market_option_price = float(row["market_option_price"])
        if market_option_price <= 0:
            report_error(errors, f"Row {row_number}: market_option_price must be > 0.")
    except ValueError:
        report_error(errors, f"Row {row_number}: market_option_price is not numeric.")

    try:
        open_interest = int(row["open_interest"])
        if open_interest <= 0:
            report_error(errors, f"Row {row_number}: open_interest must be > 0.")
    except ValueError:
        report_error(errors, f"Row {row_number}: open_interest is not an integer.")

    try:
        time_to_expiry_years = float(row["time_to_expiry_years"])
        if time_to_expiry_years <= 0:
            report_error(errors, f"Row {row_number}: time_to_expiry_years must be > 0.")
    except ValueError:
        report_error(errors, f"Row {row_number}: time_to_expiry_years is not numeric.")
        return

    try:
        quote_date = datetime.strptime(row["quote_date"], DATE_FORMAT).date()
        expiry_date = datetime.strptime(row["expiry_date"], DATE_FORMAT).date()
    except ValueError as exc:
        report_error(errors, f"Row {row_number}: date parse error: {exc}.")
        return

    if expiry_date <= quote_date:
        report_error(errors, f"Row {row_number}: expiry_date must be after quote_date.")

    try:
        days_to_expiry = int(row["days_to_expiry"])
    except ValueError:
        report_error(errors, f"Row {row_number}: days_to_expiry is not an integer.")
        return

    actual_days_to_expiry = (expiry_date - quote_date).days
    if days_to_expiry != actual_days_to_expiry:
        report_error(
            errors,
            (
                f"Row {row_number}: days_to_expiry={days_to_expiry} "
                f"does not match date difference {actual_days_to_expiry}."
            ),
        )

    expected_time_to_expiry_years = actual_days_to_expiry / 365.0
    if abs(time_to_expiry_years - expected_time_to_expiry_years) > TIME_TO_EXPIRY_TOLERANCE:
        report_error(
            errors,
            (
                f"Row {row_number}: time_to_expiry_years={time_to_expiry_years} "
                f"does not match days_to_expiry/365={expected_time_to_expiry_years:.6f} "
                f"within tolerance {TIME_TO_EXPIRY_TOLERANCE}."
            ),
        )

    overflow_counts[row["open_interest_overflow_flag"]] += 1


def main() -> int:
    if not SOURCE_FILE.exists():
        print(f"Source file not found: {SOURCE_FILE}", file=sys.stderr)
        return 1

    if not OUTPUT_FILE.exists():
        print(f"Output file not found: {OUTPUT_FILE}", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen_source_row_ids: set[str] = set()
    overflow_counts: Counter[str] = Counter()
    before_count = 0
    expected_after_count = 0
    output_row_count = 0

    with SOURCE_FILE.open("r", newline="", encoding="utf-8-sig") as source_handle:
        source_reader = csv.DictReader(source_handle)

        with OUTPUT_FILE.open("r", newline="", encoding="utf-8") as output_handle:
            output_reader = csv.DictReader(output_handle)
            actual_schema = output_reader.fieldnames or []
            if actual_schema != OUTPUT_SCHEMA:
                report_error(
                    errors,
                    (
                        "Output schema mismatch. "
                        f"Expected {OUTPUT_SCHEMA!r} but found {actual_schema!r}."
                    ),
                )

            output_iter = iter(output_reader)

            for source_row_id, source_row in enumerate(source_reader, start=1):
                before_count += 1
                if not row_matches_locked_filters(source_row):
                    continue

                expected_after_count += 1
                try:
                    output_row = next(output_iter)
                except StopIteration:
                    report_error(
                        errors,
                        (
                            "Output ended early before all filtered source rows were emitted. "
                            f"Missing output row for source_row_id {source_row_id}."
                        ),
                    )
                    break

                output_row_count += 1
                validate_output_row(
                    output_row_count,
                    output_row,
                    seen_source_row_ids,
                    overflow_counts,
                    errors,
                )

                expected_row = build_expected_output_row(source_row_id, source_row)
                if output_row != expected_row:
                    report_error(
                        errors,
                        (
                            f"Row {output_row_count}: output row does not match source row "
                            f"{source_row_id} after applying the locked transformation."
                        ),
                    )

            for extra_row in output_iter:
                output_row_count += 1
                report_error(
                    errors,
                    (
                        "Output contains extra rows beyond the filtered source set. "
                        f"First extra source_row_id value: {extra_row.get('source_row_id', '')}."
                    ),
                )
                break

    print(f"Source file: {SOURCE_FILE.name}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Rows before filtering: {before_count}")
    print(f"Rows after filtering (expected from source): {expected_after_count}")
    print(f"Rows after filtering (found in output): {output_row_count}")
    print("open_interest_overflow_flag values:")
    if overflow_counts:
        for value in sorted(overflow_counts):
            print(f"  {value}: {overflow_counts[value]}")
    else:
        print("  (none)")

    if errors:
        print("AUDIT FAILED")
        for message in errors:
            print(f"- {message}")
        return 1

    print("AUDIT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
