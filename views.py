from django.http import *
from django.shortcuts import *

def index(request):
    return render(request, 'index.html')

def func(request):
    print(request.GET.get('text', 'ffdsfdf'))
    return HttpResponse('func')
