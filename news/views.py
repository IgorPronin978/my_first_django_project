from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return HttpResponse("Привет, Мир!")


def info(request):
    return HttpResponse("Информационная страница")

def get_all_news(request):
    return render(request, "news/catalog.html")

def get_news_by_id(request, news_id):
    if news_id > 5:
        return HttpResponse('Нет таких новостей', status=404)
    return HttpResponse(f'Вы открыли новость {news_id}')