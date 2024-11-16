from django.shortcuts import render

def catalog(req):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели - Home",
    }
    return render()


def product(req):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас , мы классные",
    }
    return render()
