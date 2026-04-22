import streamlit as st
import datetime
from binance.client import Client
from config import API_KEY, API_SECRET
import pandas as pd

# --- Setup ---
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

st.title("📊 Trading Bot Dashboard")

# --- SIDEBAR INPUT ---
st.sidebar.header("⚙ Settings")

symbol = st.sidebar.selectbox(
    "Select Symbol",
    ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
)

buy_price = st.sidebar.slider("Buy Below", 1000, 100000, 60000)
sell_price = st.sidebar.slider("Sell Above", 1000, 100000, 65000)

# --- SESSION STATE ---
if "running" not in st.session_state:
    st.session_state.running = False

if "price_data" not in st.session_state:
    st.session_state.price_data = []

if "time_data" not in st.session_state:
    st.session_state.time_data = []

if "trades" not in st.session_state:
    st.session_state.trades = []

# --- BUTTONS ---
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start"):
        st.session_state.running = True

with col2:
    if st.button("⏹ Stop"):
        st.session_state.running = False

# --- FUNCTIONS ---
def get_price():
    try:
        data = client.futures_symbol_ticker(symbol=symbol)
        return float(data['price'])
    except:
        return None

def strategy(price):
    if price < buy_price:
        return "BUY"
    elif price > sell_price:
        return "SELL"
    else:
        return "HOLD"

# --- MAIN ---
if st.session_state.running:
    price = get_price()

    if price:
        decision = strategy(price)

        # Store data
        st.session_state.price_data.append(price)
        st.session_state.time_data.append(
            datetime.datetime.now().strftime("%H:%M:%S")
        )

        # Limit data size
        if len(st.session_state.price_data) > 50:
            st.session_state.price_data.pop(0)
            st.session_state.time_data.pop(0)

        # Store trades
        if decision != "HOLD":
            st.session_state.trades.append({
                "Time": datetime.datetime.now().strftime("%H:%M:%S"),
                "Action": decision,
                "Price": price
            })

        # --- DISPLAY ---
        st.metric(f"{symbol} Price", price)
        st.write(f"Decision: **{decision}**")

        # --- GRAPH ---
        st.subheader("📈 Live Price Chart")

        df = pd.DataFrame({
            "Time": st.session_state.time_data,
            "Price": st.session_state.price_data
        })

        df.set_index("Time", inplace=True)
        st.line_chart(df)

        # --- TRADES ---
        st.subheader("📊 Trade History")
        st.dataframe(st.session_state.trades)

    else:
        st.error("Error fetching price")

# --- FOOTER ---
st.caption("Interactive Trading Dashboard | Streamlit + Binance Testnet")

import time

if st.session_state.running:
    time.sleep(6)
    st.rerun()
    
import random

price = get_price()

if price is not None:
     change = random.uniform(-50, 50)  # volatility
     price = price + change
     
if "last_price" not in st.session_state:
    st.session_state.last_price = price

change = random.uniform(-30, 30)
price = st.session_state.last_price + change

st.session_state.last_price = price

import altair as alt

df = pd.DataFrame({
    "Time": st.session_state.time_data,
    "Price": st.session_state.price_data
})

chart = alt.Chart(df).mark_line().encode(
    x="Time",
    y=alt.Y("Price", scale=alt.Scale(zero=False))
)

st.altair_chart(chart, use_container_width=True)