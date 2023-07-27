from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Photo, Announcement

# Create your views here.

def home_view(request): # function view over class view for added logic
    message1 = 'hello world from the view!'
    return  render(request, 'home/home.html', {'h':message1})

class PhotoCarousel(ListView):
    context_object_name = 'data'
    template_name = 'home/home.html'
    queryset = Photo.objects.all()

class HomeView(ListView):
    context_object_name = "data"
    template_name = 'home/home.html'
    
    def get_queryset(self):
        myset = {
            "photos": Photo.objects.all(),
            "announcements": Announcement.objects.all().order_by('created')
        }
        return myset