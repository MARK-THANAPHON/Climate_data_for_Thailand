from pathlib import Path

INPUT_FILE = Path(
    "data/raw/nasa_power/"
    "nasa_power_thailand_district_daily.csv"
)

TARGET_GRID = "D0798"
TARGET_DATE = "2010-11-27"

print("=" * 70)
print("CHECK BAD ROW CONTEXT")
print("=" * 70)

found = False

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8",
    newline=""
) as f:

    header = f.readline().rstrip("\n")

    for line_number, line in enumerate(f, start=2):

        if line.startswith(f"{TARGET_GRID},"):

            parts = line.rstrip("\n").split(",")

            if len(parts) >= 4:

                date = parts[3]

                if date in [
                    "2010-11-26",
                    "2010-11-27",
                    "2010-11-28"
                ]:

                    print(
                        f"\nLine: {line_number:,}"
                    )

                    print(
                        f"Columns: {len(parts)}"
                    )

                    print(line.rstrip("\n"))

                    found = True

        # หลังจากเลยช่วงวันที่แล้ว
        if found and line.startswith("D0798,"):

            parts = line.rstrip("\n").split(",")

            if len(parts) >= 4 and parts[3] > "2010-11-28":
                break

print("\n" + "=" * 70)

if found:
    print("พบข้อมูลรอบวันที่มีปัญหา")
else:
    print("ไม่พบข้อมูลรอบวันที่มีปัญหา")

print("=" * 70)
