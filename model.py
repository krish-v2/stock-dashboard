import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_price(df):
    if "Close" not in df.columns or len(df) < 20:
        return None

    df = df.dropna()

    # Use last 50 points
    df = df.tail(50)

    X = np.arange(len(df)).reshape(-1, 1)
    y = df["Close"].values

    model = LinearRegression()
    model.fit(X, y)

    next_x = np.array([[len(df)]])
    prediction = model.predict(next_x)

    return float(prediction[0]) 