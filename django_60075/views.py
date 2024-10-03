from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('Hola Soy la vista')