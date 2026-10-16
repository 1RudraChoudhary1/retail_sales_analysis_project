"""
Retail Sales Analysis
---------------------
Step 1: Load and explore the data
Step 2: Check data quality (missing values, duplicates, invalid values)
Step 3: Clean the data
Step 4: Save the cleaned data to data/retail_cleaned.csv

Run from the project root:
    python src/retail_analysis.py
"""

from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# File paths (built relative to this file, so the script works from anywhere)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "retail.csv"
OUTPUT_PATH = BASE_DIR / "data" / "retail_cleaned.csv"


def section(title):
    """Print a heading so the output is easy to read."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ===========================================================================
# STEP 1: LOAD AND EXPLORE THE DATA
# ===========================================================================
df = pd.read_csv(INPUT_PATH)

section("First 10 rows")
print(df.head(10))

section("Last 5 rows")
print(df.tail(5))

section("Shape (rows, columns)")
print(df.shape)

section("Column names")
print(df.columns.tolist())

section("Unique cities")
print(df["City"].unique())

section("Unique products")
print(df["Product"].unique())

section("Basic statistics (numeric columns)")
print(df.describe())


# ===========================================================================
# STEP 2: CHECK DATA QUALITY
# ===========================================================================

# --- Missing values: how many blanks are there in each column? -------------
section("Missing values per column")
print(df.isnull().sum())

# --- Duplicates: rows that appear more than once ----------------------------
# duplicated() marks every repeat of an earlier row as True (the first copy is False)
section("Number of duplicate rows")
print(df.duplicated().sum())

# --- Invalid values: quantity and price should never be zero or negative ----
section("Invalid values")
zero_qty = (df["Quantity"] == 0).sum()
negative_qty = (df["Quantity"] < 0).sum()
negative_price = (df["Unit_Price"] < 0).sum()
print(f"Quantity = 0      : {zero_qty}")
print(f"Quantity < 0      : {negative_qty}")
print(f"Unit_Price < 0    : {negative_price}")


# ===========================================================================
# STEP 3: CLEAN THE DATA
# Each step is saved back into `df` so the cleaning actually sticks.
# ===========================================================================
rows_before = len(df)

# --- 3a. Remove duplicate rows (keeps the first copy of each) ---------------
df = df.drop_duplicates()
print(f"\nRemoved {rows_before - len(df)} duplicate rows")

# --- 3b. Convert Order_Date from text to a real date type -------------------
# This allows date operations later (sorting, grouping by month, etc.)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# --- 3c. Remove rows with impossible values ---------------------------------
# A negative or zero quantity/price is a data-entry error, so we drop those rows.
rows_before_invalid = len(df)
df = df[(df["Quantity"] > 0) & (df["Unit_Price"] > 0)]
print(f"Removed {rows_before_invalid - len(df)} rows with invalid Quantity/Unit_Price")

# --- 3d. Fill missing ratings with the median rating ------------------------
# The median is a safe choice: it is not pulled around by extreme values.
median_rating = df["Customer_Rating"].median()
missing_ratings = df["Customer_Rating"].isnull().sum()
df["Customer_Rating"] = df["Customer_Rating"].fillna(median_rating)
print(f"Filled {missing_ratings} missing ratings with the median ({median_rating})")

# --- 3e. Fill any missing quantities with the median ------------------------
# (Currently there are none, but this keeps the script safe for new data.)
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())


# ===========================================================================
# STEP 4: VERIFY AND SAVE
# ===========================================================================
section("Data types after cleaning")
print(df.dtypes)

section("Missing values after cleaning")
print(df.isnull().sum())

section("Cleaned data summary")
print(f"Rows before cleaning: {rows_before}")
print(f"Rows after cleaning : {len(df)}")

# index=False stops pandas from writing the row numbers as an extra column
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nCleaned data saved to: {OUTPUT_PATH}")
