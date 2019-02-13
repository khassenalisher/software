from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    text_var = 'this is my first django web app'
    return HttpResponse(text_var)


# Create your views here.
