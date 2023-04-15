from django.db import models
from .Category import Category
from .Price_filter import Filter_Price


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE, default=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)



    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()