from .models import Cart,CartProduct
from main.models import Product


class GetCart:

    def __init__(self, request) -> None:
        if request.session.get("cart_id"):
            try:
                cart = Cart.objects.get(id=int( request.session.get("cart_id")))
            except:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id 
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id 
        self.cart = cart 
        self.request = request 


    def  getvalayut(self,product,qty):
        valyuta = self.request.session.get("valyuta", 'usd')
        total_price = 0
        if valyuta == 'usd':
            total_price = product.price_usd * qty
        if valyuta == 'uzs':
            total_price = product.price_uzs * qty
        else:
            total_price = product.price_rub * qty
        return total_price       


    def add(self, product_id,qty=1):
        try:
            product = Product.objects.get(id=int(product_id))
        except:
            return {"status":"error","message":"Product does not exists", "cart_total_products":self.cart.products.count()}
        if self.cart.products.filter(product=product).exists():
            return {"status":"error","message":"The product has been added to cart", "cart_total_products":self.cart.products.count()}
        else:
            total_price = self.getvalayut(product,qty)
            cart_product =  self.cart.products.create(product=product,qty=qty,total_price=total_price)   
            self.cart.calculated_summa += total_price
            self.cart.total_summa += total_price
            self.cart.save()
            return {"status":"ok","message":"The product added to  cart" , "cart_total_products":self.cart.products.count()}


    def change(self):
        data_id = self.request.GET.get('data_id')         
        qty = self.request.GET.get('qty')
        cart = self.cart
  
        cart_product = CartProduct.objects.get(id=int(data_id))
        total_price = cart_product.product.price_rub * int(qty)
   
        if  cart.calculated_summa - cart_product.total_price < 0:
            cart.calculated_summa = 0
            cart.total_summa = 0
        else:    
            cart.calculated_summa -= cart_product.total_price
            cart.total_summa -= cart_product.total_price
        cart.save()

        cart_product.total_price = total_price
        cart_product.qty = int(qty)
        cart_product.save()
    
        cart.calculated_summa += cart_product.total_price
        cart.total_summa += cart_product.total_price
        cart.save()

        data = {
            'status':200,
            "total_price": cart_product.total_price ,
            "calculated_summa":   cart.calculated_summa ,
            "total_summa":   cart.total_summa ,
        }
        return data
    
    def delete(self):
        data_id = self.request.GET.get('data_id')
        obj = CartProduct.objects.get(id=int(data_id))
        self.cart.calculated_summa -= obj.total_price          
        self.cart.total_summa -= obj.total_price 
        self.cart.save()
        obj.delete()
        data =  {  
            'status':200,
            "calculated_summa":   self.cart.calculated_summa ,
            "total_summa":   self.cart.total_summa ,
            "products_qty":self.cart.products.count(),
        
        } 
        return data