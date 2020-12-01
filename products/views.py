from django.shortcuts import render


def products(request):
    context = {}
    return render(request, 'accounts/products.html', context)

def cart(request):
    context={}
    return render(request, 'accounts/cart.html',context)


def checkout(request):
    context={}
    return render(request,'accounts/checkout.html',context)