from django.urls import path
from home.views import home_view

app_name = 'home'

urlpatterns = [
    path('', home_view, name='homepage'),
]
