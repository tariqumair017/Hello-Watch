from django.db import models
from django.db.models.fields import CharField

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    email_address = models.EmailField()
    login_password = models.CharField(max_length=500)
    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email_address = email)
        except:
            return False
            

    def isexist(self):
        if Customer.objects.filter(email_address = self.email_address):
            return True
        else:
            return False

