from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    # /schedule/
    # path('', views.schedule_view, name='schedule'),
    path('', views.UpcomingTournamentList.as_view(), name = 'tournaments'),
    # /schedule/history
    path('history/', views.PastTournamentList.as_view(), name='history'),
    # ex: /schedule/071723/
    #path('<str:tournament_id>/', views.detail, name='detail')
    path('<pk>/', views.TournamentDetailView.as_view(), name='detail')
    
]
