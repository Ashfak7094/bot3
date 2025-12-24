import ccxt, time
from engine.coins import TOP_COINS
from engine.analyzer import analyze

def start_engine(user):
    exchange = ccxt.binance({
        "apiKey": user["api_key"],
        "secret": user["api_secret"],
        "options": {"defaultType": "spot"}
    })

    states = {}  # coin state memory

    while user["bot_active"]:

        if user["gas_wallet"] < 0.5:
            user["bot_active"] = False
            user["notice"] = "Low Gas – Bot stopped"
            break

        for symbol in TOP_COINS:
            try:
                ticker = exchange.fetch_ticker(symbol)
                price = ticker["last"]

                if symbol not in states:
                    states[symbol] = {
                        "highest": price,
                        "lowest": price,
                        "in_trade": False,
                        "buy_price": 0,
                        "qty": 0
                    }

                s = states[symbol]
                s["highest"] = max(s["highest"], price)
                s["lowest"] = min(s["lowest"], price)

                signal = analyze(price, s["highest"], s["lowest"])

                # BUY
                if signal == "BUY" and not s["in_trade"]:
                    usdt = exchange.fetch_balance()["free"]["USDT"]
                    trade_amt = user["trade_amount"]

                    if usdt >= trade_amt:
                        qty = trade_amt / price
                        order = exchange.create_market_buy_order(symbol, qty)

                        s["in_trade"] = True
                        s["buy_price"] = price
                        s["qty"] = order["amount"]
                        s["lowest"] = price

                # SELL
                if signal == "SELL" and s["in_trade"]:
                    order = exchange.create_market_sell_order(symbol, s["qty"])

                    sell_price = price
                    buy_price = s["buy_price"]
                    pnl = (sell_price - buy_price) * s["qty"]

                    if pnl > 0:
                        user["total_profit"] += pnl
                        user["gas_wallet"] -= pnl * 0.11  # gas fee

                    s["in_trade"] = False
                    s["highest"] = price

            except Exception as e:
                print(f"{symbol} error:", e)

        time.sleep(1)  # micro-cycle (safe)
