from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/<slug>/', products, name='products'),
    path('single/<int:pk>/', single, name='single'),
]