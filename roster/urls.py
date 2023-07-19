from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    # /teams/
    path('', views.roster_view, name='teams'),
    # ex: /teams/1s

]