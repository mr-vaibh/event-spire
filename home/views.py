from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Centre, Event

# Create your views here.

def index(request):
    centres = Centre.objects.all()
    context = {'centres': centres}
    return render(request, 'home/index.html', context)

def events(request, pk):
    events = Event.objects.filter(centre=pk)
    centre = get_object_or_404(Centre, pk=pk)
    
    context = {'events': events, 'centre': centre}
    return render(request, 'home/events.html', context)