from django.db import models
from .category import Category

class Menproduct(models.Model):
    image = models.ImageField(upload_to = "men/%y")
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 


    @staticmethod
    def get_products_by_id(ids):
        return Menproduct.objects.filter(id__in = ids)

    @staticmethod
    def get_all_menprods():
        return Menproduct.objects.all()

    @staticmethod
    def get_all_menprods_by_categoryid(category_id):
        if category_id:
            return Menproduct.objects.filter(category = category_id)
        else:
            return Menproduct.get_all_menprods();
