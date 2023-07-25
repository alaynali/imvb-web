from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Announcement

# Create your views here.

def home_view(request): # function view over class view for added logic
    message1 = 'hello world from the view!'
    return  render(request, 'home/home.html', {'h':message1})

class AnnouncementCarousel(ListView):
    context_object_name = 'data'
    template_name = 'home/home.html'
    queryset = Announcement.objects.all()