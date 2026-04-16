import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/flights_sample_100k.csv")

# Get an overview of the dataset
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
missing_counts = df.isnull().sum()
missing_pct = (missing_counts / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    "missing_count": missing_counts,
    "missing_pct": missing_pct
}).sort_values("missing_count", ascending=False)

# Save this missing-value summary to a CSV file for further analysis
missing_summary.to_csv("datasets/missing_summary.csv")