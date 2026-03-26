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





