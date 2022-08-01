from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse

from cart.models import Cart,CartProduct
from .cart import GetCart
# Create your views here.


class CartView(View):

    def get(self, request):
        cart = None
        if request.session.get("cart_id"):
            cart = get_object_or_404(Cart,id=int(request.session.get("cart_id")))
        context = {'cart':cart}
        return render(request, "cart.html",context)


class CartAddView(View):
    def get(self,request):
        product_id = request.GET.get('product_id')
        cart = GetCart(request)
        add_status = cart.add(product_id)
        return JsonResponse({"status":add_status['message'] ,"cart_total_products":add_status['cart_total_products']})

class CartChangeView(View):
    def get(self,request):
        data = GetCart(request).change()
        return JsonResponse(data)
    
    
class Delete_product(View):
    def get(self,request):
        data = GetCart(request)
        d = data.delete()
        return JsonResponse(d)
    
    
