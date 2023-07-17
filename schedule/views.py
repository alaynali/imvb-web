from django.shortcuts import render

# Create your views here.

def schedule_view(request):
    message = 'hello world from schedule view!'
    return render(request, 'schedule/main.html', {'hello':message})