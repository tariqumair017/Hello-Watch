from django.db import models
from .menproduct import Menproduct
from .customer import Customer
import datetime

class Request(models.Model):
    Order_ID = models.AutoField(primary_key = True)
    Delivered = models.BooleanField(default = False)

    def __str__(self):
        return str(self.Order_ID)