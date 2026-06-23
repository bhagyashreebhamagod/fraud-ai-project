import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from features import create_features

# load data
df = pd.read_csv("data/transactions.csv")

# features
df = create_features(df)

# split
X = df.drop("fraud", axis=1)
y = df["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1
)

model.fit(X_train, y_train)

# save model
joblib.dump(model, "model/model.pkl")

print("Model trained successfully")
