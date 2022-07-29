from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField("Kategoriya nomi", max_length=55)
    image = models.ImageField("Kategoriya rasmi",upload_to="category_images")
    products_qty = models.PositiveIntegerField("Tovarlari soni",default=0)
    add_size = models.BooleanField("Razmer qo'shish",default=False )
    add_color = models.BooleanField("Rang qo'shish",default=False )

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
    def __str__(self):
        return self.name    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name="Kategoriyasi", null=True,
     on_delete=models.PROTECT, related_name="subcategorys")
    name = models.CharField("SubKategoriya nomi", max_length=55)
    products_qty = models.PositiveIntegerField("Tovarlari soni",default=0)

    class Meta:
        verbose_name = "SubKategoriya"
        verbose_name_plural = "SubKategoriyalar"
    
    def __str__(self):
        return self.name 

class Colors(models.Model):
    name = models.CharField("Rang nomi", max_length=15)
    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"
    
    def __str__(self):
        return self.name 

class SIZES(models.TextChoices):
    xs = "xs", 'xs'
    s = "s", 's'
    m = "m", 'm'
    l = "l", 'l'
    xl = "xl", 'xl'



class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Kategoriyasi", on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, null=True, verbose_name="SubKategoriyasi",  on_delete=models.PROTECT)
    name = models.CharField("Tovar nomi", max_length=55)
    image = models.ImageField("Tovar rasmi",upload_to="category_images")
    qty = models.PositiveIntegerField("Ombordagi soni",default=0)
    description = models.TextField("Tovar xaqida")
    rating = models.PositiveIntegerField("Reyting",default=0)
    views = models.PositiveIntegerField("Ko'rishlar soni",default=0)
    colors = models.ManyToManyField(Colors)
    size = models.CharField("Razmeri", max_length=5, blank=True, choices=SIZES.choices)
    price_uzs = models.PositiveIntegerField("Narxi uzs", default=0)
    price_usd = models.DecimalField("Narxi usd",max_digits=8, decimal_places=2,  default=0.0)
    price_rub = models.DecimalField("Narxi rub",max_digits=8, decimal_places=2, default=0.0)
    options = RichTextField(config_name='default')



BANNER_SIZES = (
    ("Big", "big"),
    ("Medium", "medium"),
    ("Small", "small"),
)


class Banner(models.Model):
    name = models.CharField("Banner nomi", max_length=55)
    image = models.ImageField("Banner rasmi",upload_to="category_images")
    description = models.TextField("Banner teksti")
    banner_type = models.CharField("Banner turi", max_length=25, choices=BANNER_SIZES)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"
    
    def __str__(self):
        return self.name 
