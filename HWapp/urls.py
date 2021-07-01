from django.urls import path
from .import views
from .views import Login, Register, Men, Checkout, Orders, Profile
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('',views.index,name='index'),
    path('brands/',views.brands,name='brand'),
    path('404/',views.four,name='404'),
    path('checkout/',auth_middleware(Checkout.as_view()),name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('login/',Login.as_view(),name='login'),
    path('orders/',auth_middleware(Orders.as_view()),name='orders'),
    path('men/',auth_middleware(Men.as_view()),name='men'),
    path('register/',Register.as_view(),name='register'),
    path('single/',views.single,name='single'),
    path('profile/',auth_middleware(Profile.as_view()),name='profile'),

    path('logout/',views.logout,name='logout'),

    ]