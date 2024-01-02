from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'title': 'Homepage',
        'content': 'index - Главная страница'
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
