from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.utils import timezone
from django.db.models import Q

from .models import Tournament

# Create your views here.

# def schedule_view(request):
#     message = 'hello world from schedule view!'
#     tournament_list = Tournament.objects.order_by("id")
#     context = {"tournament_list": tournament_list}
#     return render(request, 'schedule/index.html', context)
    # return render(request, 'schedule/main.html', {'h': message})

def results(request):
    message = 'hello world from schedule results!'
    return render(request, 'schedule/results.html', {'h': message})

def detail(request, tournament_id):
    # message = 'tournament id ' + tournament_id
    # return render(request, 'schedule/main.html', {'h': message})
    try:
        tournament = Tournament.objects.get(id=tournament_id)
    except Tournament.DoesNotExist:
        raise Http404("Tournament does not exist")
    return render(request, 'schedule/detail.html', {'tournament': tournament})

class UpcomingTournamentList(ListView):
    template_name = 'schedule/main.html'
    queryset = Tournament.objects.filter(
        end_date__gte=timezone.now().date()
    ).order_by('start_date') #'-start_date flips the order
    paginate_by = 10

class PastTournamentList(ListView):
    template_name = 'schedule/history.html'
    queryset = Tournament.objects.filter(
        end_date__lte=timezone.now().date()
    ).order_by('-start_date')
    paginate_by = 10



