def add_indicators(df):
    if "Close" not in df.columns:
        return df

    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()

    return df