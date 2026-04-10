import pandas as pd

data = pd.read_csv("data/churn.csv")
data.dropna(inplace=True)

# Create new feature
data["customer_value"] = data["salary"] * data["purchases"]

# Save processed data
data.to_csv("data/processed.csv", index=False)

print("Data processed")