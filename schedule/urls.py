from django.urls import path
from . import views
# from schedule.views import schedule_view

app_name = 'schedule'

urlpatterns = [
    # /schedule/
    path('', views.schedule_view, name='schedule'),
    # /schedule/results
    path('results/', views.results, name='results'),
    # ex: /schedule/071723/
    path('<str:tournament_id>/', views.detail, name='detail')
]
