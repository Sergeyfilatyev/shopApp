from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(req, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    paginator = Paginator(goods, 3)
    current_page = paginator.page(3)
    context = {"title": "Home - Каталог", "goods": current_page}
    return render(req, "goods/catalog.html", context)


def product(req, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {"product": product}

    return render(req, "goods/product.html", context)
