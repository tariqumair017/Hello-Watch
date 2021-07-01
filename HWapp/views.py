from django import http
from django import views
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.menproduct import Menproduct
from .models.customer import Customer
from .models.order import Order
from .models.request import Request
from django.views import View




def index(request):
    prod = Product.get_all_products();
    return render(request,'HWapp/index.html', {'products' : prod})


def brands(request):
    return render(request,'HWapp/brands.html')


class Checkout(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        prods = Menproduct.get_products_by_id(ids)
        print(prods)
        return render(request,'HWapp/checkout.html', {'products' : prods})
    def post(self, request):
        ab = request.session['cart']
        Request.objects.create()
        max_val = Request.objects.latest('Order_ID')
        cart = request.session.get('cart')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Menproduct.get_products_by_id(list(cart.keys()))
        print(name, address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            Order.objects.create(
                Order_ID = max_val,
                customer=Customer(id=customer),
                product=product, 
                price=product.price,
                name=name, 
                address=address,
                phone=phone,
                qty=cart.get(str(product.id)))
        
        request.session['cart'] = {}

        return redirect('checkout')


class Orders(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        orderview = Order.get_orders_by_customer(customer)
        print(orderview)
        return render(request,'HWapp/orders.html', {'orders':orderview})



class Profile(View):
    def get(self, request):
        return render(request,'HWapp/profile.html')
    def post(self, request):
        pass



def contact(request):
    return render(request,'HWapp/contact.html')


def four(request):
    return render(request,'HWapp/404.html')


class Login(View):
    def get(self, request):
        return render(request,'HWapp/login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        c = Customer.get_customer_by_email(email)
        error_message = None
        if c:
            flag = check_password(password, c.login_password)
            if flag:
                request.session['customer_id'] = c.id   
                return redirect('men')
            else:
                error_message = 'Email or Password invalid !'
        else:
            error_message = 'Email or Password invalid !'

        print(email, password)
        return render(request, 'HWapp/login.html', {'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')


class Men(View):
    def post(self, request):
        prods = request.POST.get('hide_id')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            qty = cart.get(prods)
            if qty:
                if remove:
                    if qty<=1:
                        cart.pop(prods)
                    else:
                        cart[prods] = qty-1
                else:
                    cart[prods] = qty+1                  
            else:
                cart[prods] = 1
        else:
            cart = {}
            cart[prods] = 1

        request.session['cart'] = cart
        #print('CART:', request.session['cart'])
        return redirect('men')


    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        prods = None
        categories = Category.get_all_categories()
        catid = request.GET.get('items')
        if catid:
            prods = Menproduct.get_all_menprods_by_categoryid(catid)     
        else:
            prods = Menproduct.get_all_menprods();
        data = {'menproducts':prods, 'categories':categories}
        print('Your Email is: ', request.session.get('customer_email'))
        return render(request,'HWapp/men.html', data)
        
        




class Register(View):
    def get(self, request):
        return render(request,'HWapp/register.html')
    def post(self, request):
        postData = request.POST
        fname = postData.get('firstname')
        lname = postData.get('lastname')
        phonenum = postData.get('phone')
        emailaddress = postData.get('email')
        loginpassword = postData.get('password')
        #validation
        value = { 'a' : fname, 'b' : lname, 'c' : phonenum, 'd' : emailaddress }

        error_message = None
        c = Customer(first_name = fname, last_name = lname, phone_num = phonenum, email_address = emailaddress, login_password = loginpassword)
    
        error_message = self.validateCustomer(c)

        if not error_message:
            print(fname,lname,phonenum,emailaddress,loginpassword)
            c.login_password = make_password(c.login_password)
            c.register()
            return redirect('men')
        else:
            data = { 'error' : error_message, 'vls':value }
            return render(request, 'HWapp/register.html', data)
    def validateCustomer(self, c):
        error_message = None;
        if (not c.first_name):
            error_message ="First Name Required !"
        elif len(c.first_name) < 4:
            error_message = "First Name must be more than 4 character"
        elif not c.last_name:
            error_message = "Last Name Required !"
        elif len(c.last_name) < 4:
            error_message = "Last Name must be more than 4 character"
        elif not c.phone_num:
            error_message = "Phone Number Required !"
        elif len(c.phone_num) < 11:
            error_message = "Phone Number must be 11 character long"
        elif not c.email_address:
            error_message = "Email Address Required !"
        elif len(c.email_address) < 5:
            error_message = "Email must be 5 character long"
        elif len(c.login_password) < 6:
            error_message = "Password must be more than 6 character"
        elif c.isexist():
            error_message = 'Email Address already Registered..'

        #Save
        return error_message



def single(request):
    return render(request,'HWapp/single.html')