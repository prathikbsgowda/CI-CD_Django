from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, CI/CD with Django!")
