from .models import Category
from cart.models import Cart
from cart.cart import GetCart

def get_category_objects(request):
    categorys = Category.objects.all()
    cart_products_count = 0
    if  request.session.get("cart_id"):
        cart = GetCart(request).cart
        cart_products_count = cart.products.count()

    return {"categorys":categorys,"cart_products_count":cart_products_count}


    