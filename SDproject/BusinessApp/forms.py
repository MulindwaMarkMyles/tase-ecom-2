from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class BusinessUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model=models.Business
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

class ServiceForm(forms.ModelForm):
    class Meta:
        model=models.Service
        fields=['name','price','description','service_image']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
#class OrderForm(forms.ModelForm):
    #class Meta:
        #model=models.Orders
        #fields=['status']

#for contact us page
class ContactusForm(forms.ModelForm):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))