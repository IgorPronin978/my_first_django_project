from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Привет, Мир!")


def info(request):
    return HttpResponse("Информационная страница")