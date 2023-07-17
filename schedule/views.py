from django.shortcuts import render
from .models import Tournament

# Create your views here.

def schedule_view(request):
    message = 'hello world from schedule view!'
    tournament_list = Tournament.objects.order_by("start_date")

    return render(request, 'schedule/main.html', {'h':message})

def results(request):
    message = 'hello world from schedule results!'
    return render(request, 'schedule/main.html', {'h': message})

def detail(request, tournament_id):
    message = 'tournament details on ' + tournament_id + '!'
    return render(request, 'schedule/main.html', {'h': message})