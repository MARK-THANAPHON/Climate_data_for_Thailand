import csv
from pathlib import Path

INPUT_FILE = Path(
    "data/raw/nasa_power/"
    "nasa_power_thailand_district_daily.csv"
)

EXPECTED_COLUMNS = 15

print("=" * 70)
print("NASA POWER CSV INTEGRITY CHECK")
print("=" * 70)

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"ไม่พบไฟล์: {INPUT_FILE}")

print(f"File: {INPUT_FILE}")
print(
    f"Size: "
    f"{INPUT_FILE.stat().st_size / (1024**3):.2f} GB"
)

bad_count = 0
total_count = 0
first_bad_rows = []

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8",
    newline=""
) as f:

    reader = csv.reader(f)

    header = next(reader)

    print(f"\nHeader columns: {len(header)}")
    print("Header:")
    print(header)

    for line_number, row in enumerate(reader, start=2):

        total_count += 1

        if len(row) != EXPECTED_COLUMNS:

            bad_count += 1

            if len(first_bad_rows) < 20:
                first_bad_rows.append(
                    (line_number, len(row), row)
                )

print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)

print(f"Total data rows : {total_count:,}")
print(f"Bad rows        : {bad_count:,}")

if bad_count == 0:
    print("\n✅ ทุกแถวมี 15 columns ถูกต้อง")
else:
    print("\n❌ พบแถวที่มีจำนวน columns ไม่ถูกต้อง")

    print("\nFirst bad rows:")
    print("-" * 70)

    for line_number, column_count, row in first_bad_rows:
        print(
            f"Line {line_number:,} | "
            f"Columns = {column_count}"
        )
        print(row)

print("\n" + "=" * 70)
print("CHECK COMPLETED")
print("=" * 70)