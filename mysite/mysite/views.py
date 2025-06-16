# i created this file
#views.py handle the thing to be shown on webpage
from django.http import HttpResponse # all the things are retuen in form of http response
from django.shortcuts import render
def index(request):
    return HttpResponse("<h1 style='color:blue;'>You're index page</h1> <br> used url serverdomain/")

def about(request):
    return HttpResponse("This is About page, used url serverdomain/about")

from django.http import HttpResponse

def sampletxt(request):
    with open('sample.txt', 'r') as file:
        content = file.read()
    return HttpResponse(content, content_type='text/plain')

def personalNavigator(request):
    return render(request,'abc.html')