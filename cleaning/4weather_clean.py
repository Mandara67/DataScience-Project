import pandas as pd

df = pd.read_csv("datasets/weather_sample_100k.csv", low_memory=False)

print("Original shape:", df.shape)

print("----Conversions-----------------------------------")
# Convert date columns to datetime
for col in ["FL_DATE", "ORIGIN_DATE", "DEST_DATE"]:
    if col in df.columns:
        initial_type = df[col].dtype
        df[col] = pd.to_datetime(df[col], errors="coerce")
        print(f"{col} converted from {initial_type} to {df[col].dtype}")

print("-------Cleaning-----------------------------------")

# Remove all cols that are 100% null
df = df.dropna(axis=1, how="all")
print("Shape after removing fully null columns:", df.shape)

# Identify attribute columns (these appear to store observation flags / metadata rather than primary weather measurements)
attribute_cols = [col for col in df.columns if col.endswith("_ATTRIBUTES")]
print(f"Number of attribute columns: {len(attribute_cols)}")
# Build cleaned dataset without attribute columns
df_no_attr = df.drop(columns=attribute_cols)

df_no_attr.to_csv("datasets/weather_sample_100k_cleaned.csv", index=False)
print(f"Saved cleaned dataset ({df_no_attr.shape[1]} cols) to datasets/weather_sample_100k_cleaned.csv")

# A smaller list of columns that are most relevant
relevant_cols = [
    # Flight-related columns
    "FL_DATE", "AIRLINE", "AIRLINE_CODE", "FL_NUMBER",
    "ORIGIN", "ORIGIN_CITY", "DEST", "DEST_CITY",
    "CRS_DEP_TIME", "DEP_TIME", "DEP_DELAY",
    "CRS_ARR_TIME", "ARR_TIME", "ARR_DELAY",
    "CANCELLED", "DIVERTED", "DISTANCE",
    # Origin location related columns
    "ORIGIN_DATE", "ORIGIN_STATION", "ORIGIN_LATITUDE", "ORIGIN_LONGITUDE",
    "ORIGIN_PRCP", "ORIGIN_SNOW", "ORIGIN_SNWD",
    "ORIGIN_TMAX", "ORIGIN_TMIN", "ORIGIN_AWND",
    # Destination location related columns
    "DEST_DATE", "DEST_STATION", "DEST_LATITUDE", "DEST_LONGITUDE",
    "DEST_PRCP", "DEST_SNOW", "DEST_SNWD",
    "DEST_TMAX", "DEST_TMIN", "DEST_AWND"
]

# Filter the relevant columns to only those that exist in the dataset (some were dropped earlier)
missing_relevant_cols = [col for col in relevant_cols if col not in df_no_attr.columns]
print("Missing relevant columns:", missing_relevant_cols)

relevant_cols = [col for col in relevant_cols if col in df_no_attr.columns]
df_reduced = df_no_attr[relevant_cols].copy()

print("Reduced dataset shape:", df_reduced.shape)
print("Missingness in reduced dataset:")
print(df_reduced.isnull().sum().sort_values(ascending=False))

df_reduced.to_csv("datasets/weather_sample_100k_reduced.csv", index=False)
print("Saved reduced dataset to datasets/weather_sample_100k_reduced.csv")




