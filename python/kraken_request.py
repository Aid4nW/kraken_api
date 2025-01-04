import requests
from enum import Enum
from typing import Dict

BASE_URL = "https://api.kraken.com/0/"

class KrakenPublicEndpoints(Enum):
    ASSETS = "public/Assets"
    ASSET_PAIRS = "public/AssetPairs"
    TICKER = "public/Ticker"
    OHLC = "public/OHLC"
    ORDER_BOOK = "public/Depth"
    RECENT_TRADES = "public/Trades"
    SPREAD = "public/Spread"

class KrakenPrivateEndpoints(Enum):
    BALANCE = "private/Balance"
    TRADE_BALANCE = "private/TradeBalance"
    OPEN_ORDERS = "private/OpenOrders"
    CLOSED_ORDERS = "private/ClosedOrders"
    QUERY_ORDERS = "private/QueryOrders"
    TRADES_HISTORY = "private/TradesHistory"
    QUERY_TRADES = "private/QueryTrades"
    OPEN_POSITIONS = "private/OpenPositions"
    LEDGERS = "private/Ledgers"
    QUERY_LEDGERS = "private/QueryLedgers"
    TRADE_VOLUME = "private/TradeVolume"
    ADD_ORDER = "private/AddOrder"
    CANCEL_ORDER = "private/CancelOrder"
    DEPOSIT_METHODS = "private/DepositMethods"
    DEPOSIT_ADDRESSES = "private/DepositAddresses"
    DEPOSIT_STATUS = "private/DepositStatus"
    WITHDRAW_INFO = "private/WithdrawInfo"
    WITHDRAW = "private/Withdraw"
    WITHDRAW_STATUS = "private/WithdrawStatus"
    WITHDRAW_CANCEL = "private/WithdrawCancel"
    GET_WEB_SOCKET_TOKEN = "private/GetWebSocketsToken"


def request_public_ohlc(pair: str, interval: int, since: int):
    url_extension = KrakenPublicEndpoints.OHLC.value + f"?pair={pair}&interval={interval}&since={since}"
    payload = {}
    headers = {
        'Accept': 'application/json'
    }
    return make_request(url_extension, payload, headers)


def make_request(url_extension: str, payload: Dict, headers: Dict):
    return requests.request("GET", BASE_URL + url_extension, headers=headers, data=payload)
