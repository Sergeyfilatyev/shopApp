
from django.shortcuts import render

from goods.models import Categories


def index(req):

    categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели - Home",
        "categories": categories
    }
    return render(req, "main/index.html", context)


def about(req):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас , мы классные",
    }
    return render(req, "main/about.html", context)
