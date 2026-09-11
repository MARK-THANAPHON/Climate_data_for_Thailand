import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = Path(
    "data/raw/nasa_power/"
    "nasa_power_thailand_district_daily.csv"
)


# ============================================================
# 1. ตรวจสอบไฟล์
# ============================================================

print("=" * 70)
print("NASA POWER DATA CHECK")
print("=" * 70)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"ไม่พบไฟล์: {INPUT_FILE}"
    )

print(f"File: {INPUT_FILE}")

print(
    f"Size: "
    f"{INPUT_FILE.stat().st_size / (1024**3):.2f} GB"
)


# ============================================================
# 2. อ่านเฉพาะ Header
# ============================================================
#
# ไม่อ่านข้อมูลทั้งหมด
# จึงไม่ใช้ RAM จำนวนมาก
# ============================================================

header = pd.read_csv(
    INPUT_FILE,
    nrows=0
)

print("\nColumns:")
print("-" * 70)

for col in header.columns:
    print(col)


# ============================================================
# 3. อ่านข้อมูลตัวอย่าง
# ============================================================
#
# อ่านเพียง 10,000 แถว
# เพื่อดูรูปแบบข้อมูล
# ============================================================

sample = pd.read_csv(
    INPUT_FILE,
    nrows=10_000
)


print("\nSample shape:")
print(sample.shape)


print("\nSample:")
print(sample.head())


# ============================================================
# 4. ตรวจชนิดข้อมูล
# ============================================================

print("\nData types:")
print("-" * 70)

print(
    sample.dtypes
)


# ============================================================
# 5. ตรวจ Missing Value
# ============================================================

print("\nMissing values:")
print("-" * 70)

missing = sample.isna().sum()

print(
    missing[missing > 0]
)


# ============================================================
# 6. ตรวจวันที่
# ============================================================

if "date" in sample.columns:

    sample["date"] = pd.to_datetime(
        sample["date"],
        errors="coerce"
    )

    print("\nDate range in sample:")

    print(
        "Minimum:",
        sample["date"].min()
    )

    print(
        "Maximum:",
        sample["date"].max()
    )


# ============================================================
# 7. ตรวจ Grid
# ============================================================

if "grid_id" in sample.columns:

    print("\nGrid sample:")

    print(
        "Unique grids:",
        sample["grid_id"].nunique()
    )


# ============================================================
# 8. ตรวจค่าพื้นฐานของ Climate variables
# ============================================================

climate_columns = [
    "PRECTOTCORR",
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "T2MDEW",
    "RH2M",
    "WS2M"
]


available_columns = [
    col
    for col in climate_columns
    if col in sample.columns
]


print("\nClimate summary:")
print("-" * 70)

print(
    sample[available_columns].describe()
)


# ============================================================
# 9. ตรวจค่า -999
# ============================================================
#
# NASA POWER บางข้อมูลอาจใช้ค่าพิเศษ
# แทน Missing data
# ============================================================

print("\nSpecial value check:")
print("-" * 70)

for col in available_columns:

    count = (
        sample[col] == -999
    ).sum()

    print(
        f"{col}: -999 = {count:,}"
    )


# ============================================================
# 10. สรุป
# ============================================================

print("\n" + "=" * 70)

print("CHECK COMPLETED")

print("=" * 70)