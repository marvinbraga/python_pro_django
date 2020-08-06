from django.http import HttpResponse


def home(request):
    _ = request
    return HttpResponse('Hello World!')
