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
        data_id = request.GET.get('data_id')         
        qty = request.GET.get('qty')
        print(data_id)         
        print(qty)
        cart_product = CartProduct.objects.get(id=int(data_id))
        return JsonResponse({'status':200})         