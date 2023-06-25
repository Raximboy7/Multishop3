from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/<slug>/', products, name='products'),
    path('single/<int:pk>/', single, name='single'),
    path('korzinka/<>/', Korzinka, name='korzinka'),
     path('korzinka_dalet/<>/', Korzinka_dalet, name='korzinka_dalet'),
]