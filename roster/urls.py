from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    # /roster/
    path('', views.roster_view, name='roster'),
]