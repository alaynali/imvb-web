from django.shortcuts import render
from django.http import Http404, HttpRequest
from django.views.generic import ListView
from .models import Player

# Create your views here.

def roster_view(request):
    message = 'hello world from roster view!'
    return render(request, 'roster/main.html', {'h': message})

# class RosterList(ListView):
#     template_name = 'roster/main.html'
#     queryset = Player.objects.filter(team='Illini 1s').order_by('number')
#     # paginate_by = 10

class RosterList(ListView):
    context_object_name = "data"
    template_name = 'roster/main.html'
    
    def get_queryset(self):
        myset = {
            "first": Player.objects.filter(team='Illini 1s').order_by('number'),
            "second": Player.objects.filter(team='Illini 2s').order_by('number'),
            "third": Player.objects.filter(team='Illini 3s').order_by('number'),
        }
        return myset