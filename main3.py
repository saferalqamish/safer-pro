import time
import random  # فقط لمحاكاة تحليل السوق (يمكنك استبداله ببيانات حقيقية لاحقًا)

def analyze_market():
    # محاكاة تحليل السوق: يرجّع إشارة عشوائية "Buy" أو "Sell"
    trend = random.choice(["Buy", "Sell"])
    print(f"Market Trend Detected: {trend}")
    return trend

def alert_signal(signal_type):
    print(f"ALERT: {signal_type} Signal Triggered!")

if __name__ == "__main__":
    while True:
        signal = analyze_market()
        alert_signal(signal)
        time.sleep(60)  # تحليل كل دقيقة
