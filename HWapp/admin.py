from django.contrib import admin
from django.contrib.admin.decorators import register
from .models.product import Product
from .models.category import Category
from .models.menproduct import Menproduct
from .models.customer import Customer
from .models.order import Order
from .models.request import Request

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminMenproduct(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'category']

# Register your models here.

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Menproduct, AdminMenproduct)
admin.site.register(Customer)
admin.site.register(Order)
# admin.site.register(Request)




class orderItemInline(admin.TabularInline):
    model = Order
    # raw_id_fields =['Order_ID']

@admin.register(Request)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['Order_ID']
    inlines = [orderItemInline]