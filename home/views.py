from django.shortcuts import render

# Create your views here.

def home_view(request): # function view over class view for added logic
    return  render(request, 'home/main.html', {})