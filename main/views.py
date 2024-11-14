from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    context = {
        "title": "Home",
        "content": "Main page - Home",
        "list": [1, 2, 3],
        "tyr": {"first": "tert"},
        "bool": False,
    }
    return render(req, "main/index.html", context)


def about(req):
    return HttpResponse("About page")
