from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from tinymce.models import HTMLField
from django.utils import timezone
from PIL import Image

class Business(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.TextField()
    logo=models.ImageField(upload_to='business_logos/')
    photos=models.ImageField(upload_to='business_photos/',blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    business=models.ForeignKey(Business, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_points=2)
    product_image=models.ImageField(upload_to='product_media/',blank=True)
    available=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Service(models.Model):
    business=models.ForeignKey(Business, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_points=2)
    service_image=models.ImageField(upload_to='product_media/',blank=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name