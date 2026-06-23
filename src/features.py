def create_features(df):

    df["is_night"] = df["hour"].apply(lambda x: 1 if x < 6 or x > 21 else 0)

    user_avg = df.groupby("user_id")["amount"].mean()
    df["user_avg_amount"] = df["user_id"].map(user_avg)

    df["amount_diff"] = df["amount"] - df["user_avg_amount"]

    df["high_amount"] = df["amount"].apply(lambda x: 1 if x > 5000 else 0)

    return df
