
# Register your models here.
from dataclasses import fields
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(SubCategory)
class SubCategoryAdmin(admin.TabularInline):
    model = SubCategory
    readonly_fields = ("products_qty",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','products_qty')
    readonly_fields = ('products_qty',)
    search_fields = ['name']
    list_filter = ['name']
    list_display_links = ['name']
    inlines = [SubCategoryAdmin]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','subcategory',"name",'qty')
    readonly_fields = ('rating','views')
    search_fields = ['name']
    list_filter = ['category','subcategory']

admin.site.register(Colors)
admin.site.register(Banner)


