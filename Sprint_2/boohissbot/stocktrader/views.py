from django.shortcuts import render
import yfinance as yf
import time
import datetime as dt
from .models import Stock
from .forms import StockForm, RawStockForm

# Create your views here.
# This view displays the time zone search
def home_view(request):
    context = {
    }
    return render(request, "home.html", context)

# This view displays the ticker search
def stock_search_view(request):
    time_zone = request.GET.get("time_zone")
    
    context = {
        "time_zone": time_zone,
        "market_is_open": check_valid_trading_hours(time_zone),
        "search": True
    }
    return render(request, "stock_info.html", context)

# This view displays the ticker info
def stock_info_view(request):
    ticker = request.GET.get("ticker")

    # This will update or add tickers if you want
    if request.method == "POST":
        new_ticker = request.POST.get('ticker')
        if Stock.objects.filter(ticker=new_ticker).exists():
            Stock.objects.filter(ticker=new_ticker).update(ask=request.POST.get("ask_price"))
            Stock.objects.filter(ticker=new_ticker).update(bid=request.POST.get("bid_price"))
            Stock.objects.filter(ticker=new_ticker).update(owned=request.POST.get("owned"))
        else:
            Stock.objects.create(ticker=new_ticker)
            Stock.objects.filter(ticker=new_ticker).update(ask=request.POST.get("ask_price"))
            Stock.objects.filter(ticker=new_ticker).update(bid=request.POST.get("bid_price"))
            Stock.objects.filter(ticker=new_ticker).update(owned=request.POST.get("owned"))

    context = {
        "ticker": ticker,
        "ask_price": get_ask_price(ticker),
        "bid_price": get_bid_price(ticker),
        "search": False
    }
    return render(request, "stock_info.html", context)

# This view is for the save a stock page
def save_stock_view(request):
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            form = StockForm()

    context = {
        "form": form
    }
    return render(request, "stock/save_stock.html", context)

# This view allows us to look at all of the stocks that we have saved
def stock_detail_view(request):
    stocks = []

    for index in range(Stock.objects.count()):
        stocks.append(Stock.objects.get(id=index+1))

    context = {
        "stocks": stocks
    }
    return render(request, "stock/detail.html", context)

# Functions that are used in the views
# returns the current ask price of the ticker that is given
def get_ask_price(ticker):
    return yf.Ticker(ticker).info['ask']

def get_bid_price(ticker):
    return yf.Ticker(ticker).info['bid']

# checks if the trading hours are valid before starting the app
def check_valid_trading_hours(time_zone):
    current_time = int(time.strftime("%H%M"))
    weekday = dt.datetime.today().weekday()

    if (time_zone == "ET" and current_time >= 930 and current_time <= 1600) or (time_zone == "CT" and current_time >= 830 and current_time <= 1500) or (time_zone == "MT" and current_time >= 730 and current_time <= 1400) or (time_zone == "PT" and current_time >= 630 and current_time <= 1300) and (weekday != 5 and weekday != 6):
        return True
    else:
        return False # change to True for testing