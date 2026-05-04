import yfinance as yf

def get_stock_data(symbol):
    df = yf.download(
        symbol,
        period="5d",
        interval="5m",
        progress=False
    )

    # Flatten MultiIndex
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    return df