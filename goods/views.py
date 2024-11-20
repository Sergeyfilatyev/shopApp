from django.shortcuts import render

from goods.models import Products


def catalog(req):

    goods = Products.objects.all()

    context = {"title": "Home - Каталог", "goods": goods}
    return render(req, "goods/catalog.html", context)


def product(req):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас , мы классные",
    }
    return render(req, "goods/product.html")
