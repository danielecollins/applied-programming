from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'ticker',
            'ask',
            'bid',
            'owned'
        ]

class RawStockForm(forms.Form):
    ticker = forms.CharField()
    ask = forms.DecimalField()
    bid = forms.DecimalField()
    owned = forms.BooleanField()