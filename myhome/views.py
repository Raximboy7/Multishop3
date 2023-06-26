from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
def home(requests):
    ctg = Category.objects.all()
    prg = Product.objects.all()
    tex ={
        'ctg' : ctg,
        'prg' : prg
    }
    return render(requests, 'blog/index.html',tex)


def products(requests,slug = None):
    ctg = Category.objects.all()
    ctg2 = Category.objects.get(slug = slug)
    prg = Product.objects.all().filter(type_id = ctg2.id)
    
    tex ={
        'ctg' : ctg,
        'ctg2' : ctg2,
        'prg': prg,
    
    }
    return render(requests, 'blog/products.html', tex)


def single(requests, pk = None):
     products_pk = Bay.objects.all()
     ctg = Category.objects.all()
     products_pk = Product.objects.get(pk = pk)
     form = ChoiceForm()
     if requests.POST:
         forms = ChoiceForm(requests.POST or None,
                            requests.FILES or None)
         if forms.is_valid():
             root = forms.save()
             root = Bay.objects.get(pk=root.id)
             root.product = products_pk
             root.save()
             return redirect('korzinka')
         else:
             print(forms.errors)
     tex = {
        'ctg': ctg,
        'products_pk':products_pk,
        'form':form,
       
    }
     return render(requests,'blog/single.html',tex)
             
def Korzinka(requests ):
   
    products_pk = Bay.objects.all()
    
    tex = {
        
        'products_pk':products_pk,
        
    }
   
    return render(requests, 'blog/korzinka.html',tex) 

def Korzinka_dalet(requests, ):
    
    products_pk = Bay.objects.all() 
    products_pk.delete()
    return redirect('korzinka')                      