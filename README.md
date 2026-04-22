# 📊 Binance Futures Trading Bot Dashboard (Testnet)

## Overview

This project is a Python-based trading bot integrated with the Binance Futures Testnet API.
It features a real-time interactive dashboard built with Streamlit to visualize market data, trading decisions, and system activity.

The goal is to demonstrate API integration, basic trading logic, and interactive data visualization in a clean and modular system.

---

## Features

* 📡 Fetches real-time market data from Binance Futures Testnet
* 🤖 Implements a rule-based trading strategy
* 📊 Interactive dashboard using Streamlit
* 📈 Live price chart visualization
* 🧾 Trade history tracking
* 🎛 User-configurable parameters (symbol, buy/sell thresholds)
* ▶ Start/Stop bot execution

---

## Trading Strategy

A simple threshold-based approach:

* **BUY** when price < Buy Threshold
* **SELL** when price > Sell Threshold
* **HOLD** otherwise

This simulates decision-making based on basic support and resistance levels.

---

## Tech Stack

* Python
* python-binance
* Streamlit
* Pandas

---

## Project Structure

```bash
trading-bot/
│── bot.py
│── dashboard.py
│── config.py        # ignored in Git (contains API keys)
│── log.txt
│── README.md
```

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install python-binance streamlit pandas
```

---

### 2. Configure API Keys

Create a `config.py` file in the project root:

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
```

> ⚠️ **Security Note:**
> Never commit your API keys. Ensure `config.py` is listed in `.gitignore`.

---

### 3. Run the Dashboard

```bash
python -m streamlit run dashboard.py
```

---

## Notes

* This project uses the Binance **Testnet**, so no real funds are involved.
* Order execution is simulated for safety and simplicity.
* The focus is on demonstrating system design, API usage, and data visualization.

---

## Future Improvements

* Real order execution on testnet
* Advanced trading strategies (moving averages, indicators)
* Candlestick chart visualization
* Performance metrics (PnL tracking)

---

## Conclusion

This project demonstrates how to build a simple trading system by combining financial APIs, real-time data processing, and interactive dashboards.

It highlights practical skills in backend logic, API integration, and frontend visualization using Python.
