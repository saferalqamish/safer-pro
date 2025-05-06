
import time
import random

def get_market_signal():
    rsi = random.randint(0, 100)
    sma = random.randint(50, 150)
    price = random.randint(80, 120)

    if rsi < 30 and price > sma:
        signal = "BUY"
    elif rsi > 70 and price < sma:
        signal = "SELL"
    else:
        signal = "WAIT"

    return price, rsi, sma, signal

while True:
    price, rsi, sma, signal = get_market_signal()
    print(f"Price: {price}, RSI: {rsi}, SMA: {sma}, Signal: {signal}")
    time.sleep(60)
