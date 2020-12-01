from django.urls   import path
from .views import *

urlpatterns = [

    path('products/', products, name='products'),
    path('cart/',cart,name='cart'),
    path('checkout',checkout,name='checkout'),
    
]
