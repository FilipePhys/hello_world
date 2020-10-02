from django.shortcuts import render
from django.http import HttpResponse#me
from django.views.generic import TemplateView#me


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
