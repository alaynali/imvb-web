from django.shortcuts import render

# Create your views here.

def home_view(request): # function view over class view for added logic
    message1 = 'hello world from the view!'
    return  render(request, 'home/home.html', {'h':message1})