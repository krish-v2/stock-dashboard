import streamlit as st
from data import get_stock_data
from indicators import add_indicators
from model import predict_next_price
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 AI-Powered Market Dashboard")

# 🔁 Auto refresh every 10 seconds
st_autorefresh(interval=10000, key="refresh")

# Sidebar options
market = st.sidebar.selectbox("Market", ["Stocks", "Crypto", "Forex"])

if market == "Stocks":
    symbol = st.sidebar.selectbox("Select Stock", ["AAPL", "TSLA", "MSFT"])
elif market == "Crypto":
    symbol = st.sidebar.selectbox("Select Crypto", ["BTC-USD", "ETH-USD"])
else:
    symbol = st.sidebar.selectbox("Select Forex", ["USDINR=X", "EURUSD=X"])

# Fetch data
df = get_stock_data(symbol)

if df.empty:
    st.error("No data available")
else:
    df = add_indicators(df)

    st.subheader(f"{symbol} Price Chart")

    cols = [c for c in ["Close", "MA20", "MA50"] if c in df.columns]
    st.line_chart(df[cols])

    # 🤖 AI Prediction
    prediction = predict_next_price(df)

    if prediction:
        current_price = df["Close"].iloc[-1]

        st.metric(
            label="Predicted Next Price",
            value=f"{prediction:.2f}",
            delta=f"{prediction - current_price:.2f}"
        )

    # Raw data
    with st.expander("View Raw Data"):
        st.dataframe(df.tail(50))