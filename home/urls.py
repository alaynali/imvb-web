from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.AnnouncementCarousel.as_view(), name='homepage'),
]
