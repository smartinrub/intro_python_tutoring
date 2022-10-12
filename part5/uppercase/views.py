from django.http import HttpResponse


def toUpperCase(request, name: str):
    return HttpResponse(name.upper())
