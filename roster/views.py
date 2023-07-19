from django.shortcuts import render
from django.http import Http404, HttpRequest

# Create your views here.

def roster_view(request):
    message = 'hello world from roster view!'
    return render(request, 'roster/main.html', {'h': message})
