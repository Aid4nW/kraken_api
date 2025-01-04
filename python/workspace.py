import pandas as pd
from kraken_api import KrakenAPI

if __name__ == "__main__":
    kraken_obj = KrakenAPI()
    data = kraken_obj.get_coin_pair_data("TBTCEUR", 21600, 0).json()
    columns = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
    content = data["result"]["TBTCEUR"]
    dataframe = pd.DataFrame(content, columns=columns)

    # Set the time as the index
    dataframe.set_index("time", inplace=True)

    # Convert data to revelant types
    dataframe.index = pd.to_datetime(dataframe.index, unit="s")
    dataframe["open"] = pd.to_numeric(dataframe["open"])
    
    # Reverse the dataframe to have the most recent data at the start
    dataframe = dataframe.iloc[::-1]

    # Calculate the Simple Moving Average
    dataframe["SMA"] = dataframe["open"].rolling(10).mean()

    figure = dataframe.filter(items=["SMA", "open"]).plot(title='BTC/EUR exchange rate', figsize=(20, 12))
    figure.get_figure().savefig("btc_eur.pdf")
