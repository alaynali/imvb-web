from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView

from .models import Tournament

# Create your views here.

def schedule_view(request):
    message = 'hello world from schedule view!'
    tournament_list = Tournament.objects.order_by("id")
    context = {"tournament_list": tournament_list}
    return render(request, 'schedule/index.html', context)
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

class TournamentListView(ListView):
    template_name = 'schedule/main.html'
    queryset = Tournament.objects.order_by('start_date') #'-start_date flips the order
    paginate_by = 10
