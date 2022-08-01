from django.urls import path
from .views import *


app_name = "main"



urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('shop', ShopView.as_view(), name="shop" ),
    path('contact', ContactView.as_view(), name="contact" ),
]
