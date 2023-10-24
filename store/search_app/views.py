from django.shortcuts import render

# Create your views here.
from storeapp.models import Products
from django.db.models import Q


def SearchResult(request):
    products=None
    query=None
    if request.method == "POST":

        query=request.POST['searched']
        products=Products.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))

    return  render(request,'search.html',{'query':query,'products': products})