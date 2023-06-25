from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name
        
        
class Product(models.Model):
    name = models.CharField(max_length=222)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = " so'm "
    RU = "P"
    ENG = "$"
    the_price = (
        (UZ,"so'm"),
        (RU,"P"),
        (ENG,"$"), 
    )
    price_type = models.CharField(max_length=10,choices=the_price,default="so'm")
    price = models.IntegerField()
    image = models.ImageField()
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Bay(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null= True)
    ALL_SIZES= (
        ("36","36"),
        ("37","37"),
        ("38","38"),
        ("39","39"),
        ("40","40"),
        ("41","41"),
        ("42","42"),
        ("43","43"),
        ("44","44"),
    )
    size = models.CharField(max_length=100, choices=ALL_SIZES)
    ALL_VALUES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        
    )
    how = models.CharField(max_length=100,choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField(blank=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
    def get_size(self):
        return self.price * self.ALL_SIZES