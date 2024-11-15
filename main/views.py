from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели - Home",
    }
    return render(req, "main/index.html", context)


def about(req):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас , мы классные",
    }
    return render(req, "main/about.html", context)
