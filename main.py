

def analyze_market():
    # منطق التحليل هنا
    signal_type = "شراء"  # مثال
    print(f"تنبيه: {signal_type}")
    return signal_type

def alert_signal(signal_type):
    print(f"تنبيه: {signal_type}")

if __name__ == "__main__":
    while True:
        signal = analyze_market()
        alert_signal(signal)
        time.sleep(60)  # تحليل كل دقيقة

