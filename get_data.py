import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

csvfile = open('Feb-Jul2021_4hREEF.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# This will pull the price data for REEF/USDT from February to July 2021.
candlesticks = client.get_historical_klines("REEFUSDT", Client.KLINE_INTERVAL_4HOUR, "01 Feb, 2021", "30 Jul, 2021")

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()

