# Retail Sales Analysis

A beginner-friendly data exploration and cleaning project on a retail sales dataset, built with Python (pandas).

## Project Structure

```
retail-sales-analysis/
├── data/
│   ├── retail.csv            # Raw dataset (153 orders)
│   └── retail_cleaned.csv    # Cleaned output (created by the script)
├── src/
│   └── retail_analysis.py    # Analysis script
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of the order |
| Customer_Name | Customer name |
| City | City of the order |
| Category | Product category (e.g. Grocery, Clothing) |
| Product | Product name |
| Quantity | Units ordered |
| Unit_Price | Price per unit |
| Discount | Discount applied |
| Payment_Mode | Payment method (e.g. Cash, Debit Card) |
| Customer_Rating | Rating given by customer (some missing) |

## What the Script Does

**1. Explore** – previews the data, lists unique cities and products, prints summary statistics.

**2. Check quality** – counts missing values, duplicate rows, and zero/negative quantities or prices.

**3. Clean**
- Removes duplicate rows (3 found)
- Converts `Order_Date` to a proper datetime type
- Drops rows with zero/negative `Quantity` or `Unit_Price` (4 found)
- Fills missing `Customer_Rating` values (9 found) with the median rating

**4. Save** – writes the cleaned data (146 rows) to `data/retail_cleaned.csv`.

## How to Run

```bash
git clone https://github.com/<your-username>/retail-sales-analysis.git
cd retail-sales-analysis
pip install -r requirements.txt
python src/retail_analysis.py
```

## Tech Stack

Python · pandas
