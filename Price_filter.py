from django.db import models


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('100 to 200', '100 to 200'),
        ('200 to 300', '200 to 300'),
        ('300 to 500', '300 to 500'),
        ('500 to 1000', '500 to 1000'),
        ('1000 to 3000', '1000 to 3000'),
        ('3000 to 5000', '3000 to 5000'),
        ('Above 5000', 'Above 5000'),
    )

    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price
