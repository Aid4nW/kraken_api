from kraken_request import KrakenRequest

class KrakenAPI:
    def __init__(self):
        self.requester = KrakenRequest()

    def get_coin_pair_data(self, coinpair: str, interval: int, since: int):
        return self.requester.request_public_ohlc(coinpair, interval, since)