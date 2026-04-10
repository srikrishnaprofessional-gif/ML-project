import pandas as pd
import numpy as np

n = 10000  # number of rows

data = pd.DataFrame({
    "age": np.random.randint(18, 60, n),
    "salary": np.random.randint(20000, 120000, n),
    "purchases": np.random.randint(0, 20, n)
})

# Create churn logic (simple rule-based)
data["churn"] = ((data["salary"] < 50000) & (data["purchases"] < 5)).astype(int)

data.to_csv("data/churn.csv", index=False)