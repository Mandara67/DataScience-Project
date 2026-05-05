import pandas as pd

#  After inspecting, we can change object type to usable types
df = pd.read_csv("datasets/flights_sample_100k.csv")
print("----Conversions-----------------------------------")

# Convert flight date from object/string to datetime
initial_type = df["FL_DATE"].dtype
df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")
print("FL_DATE converted from " + str(initial_type) + " to", df["FL_DATE"].dtype)

# Convert binary indicator columns to integer
initial_type = df["CANCELLED"].dtype
df["CANCELLED"] = df["CANCELLED"].astype(int)
df["DIVERTED"] = df["DIVERTED"].astype(int)
print("CANCELLED and DIVERTED converted from " + str(initial_type) + " to", df["CANCELLED"].dtype)


print("----Feature Engineering-----------------------------------")

# Create new features
df["YEAR"] = df["FL_DATE"].dt.year # Extract year from flight date
df["MONTH"] = df["FL_DATE"].dt.month # Extract month from flight date
df["DAY_OF_WEEK"] = df["FL_DATE"].dt.dayofweek # Extract day of week from flight date
df["IS_WEEKEND"] = df["DAY_OF_WEEK"].isin([5, 6]).astype(int) # Create binary feature for weekend flights (saturday is 5, sunday is 6)

# Create binary indicator columns 
df["ARR_DELAYED"] = (df["ARR_DELAY"] > 10).astype(int) # If arrival delayed, set to 1, else 0
df["DEP_DELAYED"] = (df["DEP_DELAY"] > 10).astype(int) # If departure delayed, set to 1, else 0

print(df[["FL_DATE", "YEAR", "MONTH", "DAY_OF_WEEK", "IS_WEEKEND", "ARR_DELAY", "ARR_DELAYED", "DEP_DELAYED"]].head())

# Save cleaned dataset as a new file
output_path = "datasets/flights_sample_100k_cleaned.csv"
df.to_csv(output_path, index=False)
print("\nSaved cleaned dataset to:", output_path)



