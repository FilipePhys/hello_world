from django.shortcuts import render
from django.http import HttpResponse#me

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World! É com vc mesmo Pableira!!!')
