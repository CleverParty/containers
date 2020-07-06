from django.http import HttpResponse


def index(request):
    return HttpResponse("ping to /holder works!")