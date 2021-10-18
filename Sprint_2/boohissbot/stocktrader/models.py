from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=5)
    ask = models.DecimalField(max_digits=10, decimal_places=2)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    owned = models.BooleanField() 
    # when adding a field you need to set it to null=True or add a default value. You can add a default value via the console when you run py manage.py makemigrations
    # always run py manage.py makemigrations then py manage.py migrate when adding tables