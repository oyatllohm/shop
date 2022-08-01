from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


class HomeView(View):
    def get(self, request):
        big_banner = Banner.objects.filter(banner_type='Big').order_by('-id')[:3]
        small_banners = Banner.objects.filter(banner_type='Small').order_by('-id')[:3]
        products = Product.objects.all().order_by('views')
        
        contest = {"big_banner":big_banner,"small_banners":small_banners}
        contest['products'] = products
        return render(request, "index.html",contest)
    
class ShopView(View):
    def get(self,request):
        return render(request=request, template_name='shop.html')
    
class ContactView(View):
    def get(self,request):
        return render(request=request, template_name='contact.html')