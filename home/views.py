from django.shortcuts import render
from django.http import HttpResponse
from .models import Centre, Event

# Create your views here.

def index(request):
    centres = Centre.objects.all()
    context = {'centres': centres}
    return render(request, 'home/index.html', context)

def events(request, pk):
    events = Event.objects.filter(centre=pk)
    context = {'events': events}
    return render(request, 'home/events.html', context)