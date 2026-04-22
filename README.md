# Binance Futures Trading Bot (Testnet)

## Overview

This project is a simple trading bot built using Python and Binance Futures Testnet API.

## Features

* Fetches real-time BTCUSDT price
* Implements a basic trading strategy
* Simulates order execution
* Runs continuously in a loop

## Strategy

* BUY when price < 60000
* SELL when price > 65000
* HOLD otherwise

## Setup Instructions

1. Install dependencies:
   pip install python-binance

2. Run the bot:
   python bot.py

## Note

Due to Binance Testnet authentication issues, order execution is simulated while maintaining full API integration for market data.