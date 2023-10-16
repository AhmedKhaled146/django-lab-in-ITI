from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Track
# Create your views here.


def index(request):
    all_tracks = Track.objects.all()
    return render(request, 'track/list.html', context={'all_tracks': all_tracks})

def insert(request):
    if request.method == 'POST':
        track_name = request.POST.get('name', None)

        if track_name:
            response = Track(
                name=track_name,
            )
            response.save()
            messages.success(request, f'Track {track_name} added successfully.')
            return HttpResponseRedirect('/track/')  # Redirect to the index page
        else:
            messages.error(request, 'Track Name is required')  # Fixed typo here

    return render(request, 'track/add.html')


def delete(request, id):
    Track.objects.filter(id=id).delete()
    return HttpResponseRedirect('/track/')  # Redirect to the index page
