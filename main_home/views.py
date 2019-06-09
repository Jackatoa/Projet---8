from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author'     : 'CoreyMS',
        'title'      : 'Blog Post1',
        'content'    : 'First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author'     : 'JEANNE DARC',
        'title'      : 'Blog Post2',
        'content'    : 'SECOND content',
        'date_posted': 'August 99, 2099'
    }
]


# Create your views here.

def home(request):
    return render(request, 'main_home/home.html')


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'main_home/test.html', context, {'title': 'About'})
