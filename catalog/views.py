from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Product


def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog/catalog.html", {"products": products})


def new_products(request):
    week_ago = timezone.now() - timedelta(days=7)
    products = Product.objects.filter(created_at__gte=week_ago)
    return render(request, "catalog/new.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/detail.html", {"product": product})
