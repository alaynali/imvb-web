from django.shortcuts import render
from django.http import Http404, HttpRequest

# Create your views here.

def roster_view(request):
    return HttpRequest("hello!")
