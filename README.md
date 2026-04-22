# Binance Futures Trading Bot Dashboard (Testnet)

## Overview

This project is a Python-based trading bot integrated with Binance Futures Testnet.
It includes a real-time interactive dashboard built using Streamlit to visualize market data, trading decisions, and system activity.

---

## Features

* 📡 Fetches real-time market data from Binance Futures Testnet
* 🤖 Implements a rule-based trading strategy
* 📊 Interactive Streamlit dashboard
* 📈 Live price chart visualization
* 🧾 Trade history tracking
* 🎛 User-configurable parameters (symbol, buy/sell thresholds)
* ▶ Start/Stop bot controls

---

## Strategy

A simple threshold-based strategy:

* BUY when price < Buy Threshold
* SELL when price > Sell Threshold
* HOLD otherwise

This approach simulates decision-making based on support and resistance levels.

---

## Tech Stack

* Python
* python-binance
* Streamlit
* Pandas

---

## Project Structure

```
trading-bot/
│── bot.py
│── dashboard.py
│── config.py (ignored in Git)
│── log.txt
│── README.md
```

---

## Setup Instructions

1. Install dependencies:

```
pip install python-binance streamlit pandas
```

2. Add your Binance Testnet API keys in `config.py`:

```
API_KEY = "your_api_key"
API_SECRET = "your_secret_key"
```

3. Run the dashboard:

```
python -m streamlit run dashboard.py
```

---

## Notes

* This project uses Binance **Testnet**, so no real funds are involved.
* Order execution is simulated for safety and simplicity.
* The focus is on API integration, system design, and data visualization.

---

## Future Improvements

* Real order execution on testnet
* Advanced strategies (moving averages, indicators)
* Candlestick charts
* Performance metrics (PnL tracking)

---

## Conclusion

This project demonstrates the integration of financial APIs, real-time data processing, and interactive dashboards to simulate a trading system.
