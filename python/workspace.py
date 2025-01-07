from kraken_api import KrakenAPI

if __name__ == "__main__":
    kraken_obj = KrakenAPI()
    dataframe = kraken_obj.get_coin_pair_ohlc("TBTCEUR", 21600, 0)

    # Calculate the Simple Moving Average
    dataframe["SMA"] = dataframe["open"].rolling(10).mean()

    figure = dataframe.filter(items=["SMA", "open"]).plot(title='BTC/EUR exchange rate', figsize=(20, 12))
    figure.get_figure().savefig("btc_eur.pdf")
