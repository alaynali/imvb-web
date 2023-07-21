from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    # /schedule/
    # path('', views.schedule_view, name='schedule'),
    path('', views.TournamentListView.as_view(), name = 'list'),
    # /schedule/results
    path('results/', views.results, name='results'),
    # ex: /schedule/071723/
    path('<str:tournament_id>/', views.detail, name='detail')
    
]
