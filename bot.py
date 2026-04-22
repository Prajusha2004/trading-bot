from binance.client import Client
from config import API_KEY, API_SECRET
import time
import datetime

# --- Setup ---
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print("Connected to Binance Testnet")
print(client.futures_ping())

# --- Logging Function ---
def log(msg):
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    full_msg = f"[{timestamp}] {msg}"
    
    print(full_msg)
    
    with open("log.txt", "a") as f:
        f.write(full_msg + "\n")

# --- Get Price ---
def get_price(symbol="BTCUSDT"):
    try:
        data = client.futures_symbol_ticker(symbol=symbol)
        return float(data['price'])
    except Exception as e:
        log(f"ERROR fetching price: {e}")
        return None

# --- Strategy ---
def strategy(price):
    if price < 60000:
        return "BUY"
    elif price > 65000:
        return "SELL"
    else:
        return "HOLD"

# --- Place Order (Simulated) ---
def place_order(action):
    log(f"[SIMULATED ORDER] {action} BTCUSDT")

# --- Main Loop ---
last_decision = None

while True:
    price = get_price()

    if price is None:
        log("Retrying...")
        time.sleep(5)
        continue

    decision = strategy(price)

    log(f"Price: {price}")
    log(f"Decision: {decision}")

    if decision != last_decision and decision != "HOLD":
        place_order(decision)

    last_decision = decision

    time.sleep(10)