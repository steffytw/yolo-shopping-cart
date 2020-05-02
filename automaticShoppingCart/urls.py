from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('register',views.registrationpage,name="registrationpage"),
    path('cart',views.cart,name="cart"),
    path('deleteProduct/<id>',views.cart,name="deleteProduct"),

    
    ]