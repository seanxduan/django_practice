from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. POLLS POLLS POLLS index.")