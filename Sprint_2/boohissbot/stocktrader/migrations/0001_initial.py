# Generated by Django 3.2.8 on 2021-10-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('ask', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bid', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
