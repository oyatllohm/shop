from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product','qty','total_price']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['calculated_summa','sale','total_summa']