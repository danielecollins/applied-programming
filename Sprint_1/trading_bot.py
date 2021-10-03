import yfinance as yf
import time

class Stock_info:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_ask_price(self):
        return yf.Ticker(self.ticker).info['ask']

    def get_bid_price(self):
        return yf.Ticker(self.ticker).info['bid']

time_zone = input("What is your time zone? (ET, CT, MT, or PT) ").upper()

while time_zone != "ET" and time_zone != "MT" and time_zone != "CT" and time_zone != "PT":
    time_zone = input("Invalid time zone. What is your time zone? (ET, CT, MT, or PT) ").upper()


def check_time(time_zone):
    current_time = int(time.strftime("%H%M"))

    if (time_zone == "ET" and current_time >= 930 and current_time <= 1600) or (time_zone == "CT" and current_time >= 830 and current_time <= 1500) or (time_zone == "MT" and current_time >= 730 and current_time <= 1400) or (time_zone == "PT" and current_time >= 630 and current_time <= 1300):
        market_is_open = True
    else:
        market_is_open = False
    return market_is_open

while check_time(time_zone):
    stock = Stock_info(input("What ticker would you like to get the ask price for? "))
    print(stock.get_ask_price())

print("The market is closed.")