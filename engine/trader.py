from binance.client import Client
from engine.analyzer import analyze

def trade(user, symbol, qty):
    if not user.api_key or not user.api_secret:
        return "API NOT CONNECTED"

    if user.gas_wallet < 0.01:
        return "INSUFFICIENT GAS"

    client = Client(user.api_key, user.api_secret)
    price = float(client.get_symbol_ticker(symbol=symbol)['price'])

    levels = analyze(price)

    client.order_market_buy(symbol=symbol, quantity=qty)
    client.order_limit_sell(
        symbol=symbol,
        quantity=qty,
        price=round(levels['sell'], 2)
    )

    user.gas_wallet -= 0.01
    return "TRADE EXECUTED"
