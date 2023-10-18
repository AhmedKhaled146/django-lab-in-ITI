from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Track
from .forms import AddNewTrack
# Create your views here.

@login_required
def index(request):
    all_tracks = Track.objects.all()
    return render(request, 'track/list.html', context={'all_tracks': all_tracks})

# Using model form

@login_required
def insert(request):
    if request.method == 'POST':
        track_name = AddNewTrack(request.POST)
        if track_name.is_valid():
            track_name.save()
            track_name = track_name.cleaned_data['name']
            messages.success(request, f'Track {track_name} added successfully.')
            return HttpResponseRedirect('/track/')  # Redirect to the index page
        else:
            messages.error(request, 'Track Name is required')  # Fixed typo here
    else:
        track_name = AddNewTrack()

    return render(request,'track/add.html', context={'form': AddNewTrack()})




# # Generic

# def insert(request):
#     if request.method == 'POST':
#         track_name = request.POST.get('name', None)

#         if track_name:
#             response = Track(
#                 name=track_name,
#             )
#             response.save()
#             messages.success(request, f'Track {track_name} added successfully.')
#             return HttpResponseRedirect('/track/')  # Redirect to the index page
#         else:
#             messages.error(request, 'Track Name is required')  # Fixed typo here

#     return render(request, 'track/add.html')

@login_required
def delete(request, id):
    Track.objects.filter(id=id).delete()
    return HttpResponseRedirect('/track/')  # Redirect to the index page

@login_required
def update(request, id):
    track = get_object_or_404(Track, pk=id)
    if request.method == 'POST':
        track.name = request.POST['name']
        track.save()
        return HttpResponseRedirect('/track/') # Redirect to the index page
    return render(request, 'track/update.html', {'track': track})
