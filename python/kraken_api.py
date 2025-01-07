from requests import Response

import pandas as pd

from kraken_request import KrakenRequest

class KrakenAPI:
    def __init__(self):
        self.requester = KrakenRequest()

    def get_coin_pair_ohlc(self, coinpair: str, interval: int, since: int):
        response = self.requester.request_public_ohlc(coinpair, interval, since).json()
        return self.create_dataframe_from_ohlc_data_response(response, coinpair)
    
    def create_dataframe_from_ohlc_data_response(self, response: Response, coinpair: str) -> pd.DataFrame:
        columns = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
        content = response["result"][f"{coinpair}"]
        dataframe = pd.DataFrame(content, columns=columns)

        # Set the time as the index
        dataframe.set_index("time", inplace=True)

        # Convert data to revelant types
        dataframe.index = pd.to_datetime(dataframe.index, unit="s")
        dataframe["open"] = pd.to_numeric(dataframe["open"])

        # Reverse the dataframe to have the most recent data at the start
        dataframe = dataframe.iloc[::-1]

        return dataframe
