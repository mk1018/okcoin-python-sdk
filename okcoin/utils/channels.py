from types import SimpleNamespace
from okcoin.utils.interval import Interval


# Private channels
def private_account(currency: str) -> str:
    return f"spot/account:{currency}"


def private_order(base_currency: str, quote_currency: str) -> str:
    return f"spot/order:{base_currency}-{quote_currency}"


def private_order_algo(base_currency: str, quote_currency: str) -> str:
    return f"spot/order_algo:{base_currency}-{quote_currency}"


# Public channels
def public_ticker(base_currency: str, quote_currency: str) -> str:
    return f"spot/ticker:{base_currency}-{quote_currency}"


def public_candle(interval: Interval, base_currency: str, quote_currency: str) -> str:
    return f"spot/candle{interval.value}:{base_currency}-{quote_currency}"


def public_trade(base_currency: str, quote_currency: str) -> str:
    return f"spot/trade:{base_currency}-{quote_currency}"


def public_depth5(base_currency: str, quote_currency: str) -> str:
    return f"spot/depth5:{base_currency}-{quote_currency}"


def public_depth(base_currency: str, quote_currency: str) -> str:
    return f"spot/depth:{base_currency}-{quote_currency}"


PRIVATE_FUNCTIONS = SimpleNamespace(
    account=private_account,
    order=private_order,
    order_algo=private_order_algo,
)

PUBLIC_FUNCTIONS = SimpleNamespace(
    ticker=public_ticker,
    candle=public_candle,
    trade=public_trade,
    depth5=public_depth5,
    depth=public_depth,
)
