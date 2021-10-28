from django.shortcuts import render
import yfinance as yf
import time
import datetime as dt

# Create your views here.
# This view displays the time zone search
def home_view(request, *args, **kwargs):
    my_context = {
    }
    return render(request, "home.html", my_context)

# This view displays the ticker search
def stock_search_view(request):
    time_zone = request.GET.get("time_zone")
    
    my_context = {
        "time_zone": time_zone,
        "market_is_open": check_valid_trading_hours(time_zone),
        "search": True,
    }
    return render(request, "stock_info.html", my_context)

# This view displays the ticker info
def stock_info_view(request):
    ticker = request.GET.get("ticker")

    my_context = {
        "ticker": ticker,
        "ask_price": get_ask_price(ticker),
        "search": False,
    }
    return render(request, "stock_info.html", my_context)

# returns the current ask price of the ticker that is given
def get_ask_price(ticker):
    return yf.Ticker(ticker).info['ask']

# checks if the trading hours are valid before starting the app
def check_valid_trading_hours(time_zone):
    current_time = int(time.strftime("%H%M"))
    weekday = dt.datetime.today().weekday()

    if (time_zone == "ET" and current_time >= 930 and current_time <= 1600) or (time_zone == "CT" and current_time >= 830 and current_time <= 1500) or (time_zone == "MT" and current_time >= 730 and current_time <= 1400) or (time_zone == "PT" and current_time >= 630 and current_time <= 1300) and (weekday != 5 and weekday != 6):
        return True
    else:
        return False # change to True for testing