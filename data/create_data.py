import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "user_id": np.random.randint(1, 6, 100),
    "amount": np.random.randint(100, 10000, 100),
    "hour": np.random.randint(0, 24, 100),
    "location_match": np.random.randint(0, 2, 100)
})

df["fraud"] = (
    (df["amount"] > 7000) |
    (df["hour"] < 5) |
    (df["location_match"] == 0)
).astype(int)

df.to_csv("data/transactions.csv", index=False)

print("Dataset created")
