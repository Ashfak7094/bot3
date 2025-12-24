def analyze(price):
    return {
        "buy": price * 0.999,
        "sell": price * 1.001,
        "stop": price * 0.9985
    }
