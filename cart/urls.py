from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from .views import *

app_name = 'cart'

urlpatterns = [
    
    path('', CartView.as_view(), name="cart_view"),
    path('add', CartAddView.as_view(), name="cart_add"),
    path('change_product', CartChangeView.as_view(), name="change_product"),
]    
