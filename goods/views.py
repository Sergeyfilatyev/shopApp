from django.shortcuts import render

from goods.models import Products


def catalog(req):

    goods = Products.objects.all()

    context = {"title": "Home - Каталог", "goods": goods}
    return render(req, "goods/catalog.html", context)


def product(req,product_slug):
    
    product=Products.objects.get(slug=product_slug)

    context={
    "product": product
}    

    return render(req, "goods/product.html",context)
