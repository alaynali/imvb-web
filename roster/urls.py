from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    # /teams/
    # path('', views.roster_view, name='teams'),
    path('', views.RosterList.as_view(), name = 'roster'),
    # ex: /teams/1s

]