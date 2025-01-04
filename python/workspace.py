from kraken_request import request_public_ohlc

print(request_public_ohlc("TBTCEUR", 21600, 0).text)