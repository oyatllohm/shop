from django.db import models
from main.models import Product
# Create your models here.



class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_products")
    qty = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Savatcha tovari"
        verbose_name_plural = "Savatcha tovarlari"
    
    def __str__(self):
        return self.product.name 


class Cart(models.Model):
    products = models.ManyToManyField(CartProduct)
    calculated_summa = models.PositiveIntegerField(default=0)
    sale = models.PositiveIntegerField(default=0)
    shipping = models.PositiveIntegerField(default=0)
    total_summa = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = "Savatcha "
        verbose_name_plural = "Savatchalar"
    
    def __str__(self):
        return str(self.total_summa )




