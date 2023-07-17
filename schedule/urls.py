from django.urls import path
from schedule.views import schedule_view

app_name = 'schedule'

urlpatterns = [
    path('', schedule_view, name='schedule'),
]
