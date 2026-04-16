import pandas as pd

# Load your CSV file
df = pd.read_csv('datasets/weather_sample_100k.csv')

# Number of columns and rows (100121 rows, 424 cols)
num_rows, num_cols = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Identify attribute columns (these don't contain actual weather data, but flags, metadata, etc.)
num_attribute_cols = 0
for col in df.columns:
    if col.endswith("_ATTRIBUTES"):
        num_attribute_cols += 1
print(f"Number of attribute columns: {num_attribute_cols}")

# Check for missing values
missing_counts = df.isnull().sum()
missing_pct = (missing_counts / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    "missing_count": missing_counts,
    "missing_pct": missing_pct
}).sort_values("missing_count", ascending=False)

print(missing_summary.head(30))
missing_summary.to_csv("datasets/missing_summary_weather.csv")




