from django.db import models
from .menproduct import Menproduct
from .customer import Customer
from .request import Request
import datetime


class Order(models.Model):
    Order_ID = models.ForeignKey(Request, on_delete = models.CASCADE, null = True)
    product = models.ForeignKey(Menproduct, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.IntegerField()
    name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)




    def placeorder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
