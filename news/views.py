from django.http import HttpResponse
from django.shortcuts import render


info = {
    "users_count": 1,
    "news_count": 5,
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/news/catalog/",
         "url_name": "catalog"}
    ]
}

# Create your views here.
def main(request):
    return HttpResponse("Привет, Мир!")


def about(request):
    return HttpResponse("Информационная страница")

def catalog(request):
    return HttpResponse('Каталог новостей')

def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")

def get_all_news(request):
    return render(request, "news/catalog.html", context=info)

def get_news_by_id(request, news_id):
    if news_id > 5:
        return HttpResponse('Нет таких новостей', status=404)
    return HttpResponse(f'Вы открыли новость {news_id}')