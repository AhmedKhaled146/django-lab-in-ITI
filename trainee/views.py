from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.views import View




def list(request):
    all_trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'all_trainees': all_trainees})


def delete(request, id):
    Trainee.objects.filter(id=id).delete()
    messages.success(request, 'Trainee deleted successfully.')
    return HttpResponseRedirect('/trainee/')

def update(request, id):
    trainee = get_object_or_404(Trainee, pk=id)
    if request.method == 'POST':
        trainee.name = request.POST['name']
        trainee.bdate = request.POST['bdate']
        track_id = request.POST['track']
        track = Track.objects.get(pk=track_id)
        trainee.track = track  # Update the trainee's track field

        trainee.save()
        messages.success(request, f'Trainee {trainee.name} updated successfully.')
        return HttpResponseRedirect('/trainee/')
    return render(request, 'trainee/update.html', {'trainee': trainee,
                                                   'tracks': Track.objects.all()})


# def insert(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         bdate = request.POST['bdate']
#         track_id = request.POST['track']

#         track = Track.objects.get(pk=track_id)

#         Trainee.objects.create(name=name, track=track, bdate=bdate)

#         messages.success(request, f'Trainee {name} added successfully.')
#         return HttpResponseRedirect('/trainee/')
#     return render(request, 'trainee/add.html', {'tracks': Track.objects.all()})


class InsertTrainee(View):

    def get(self, request):
        return render(request, 'trainee/add.html', {'tracks': Track.objects.all(),
                                                    'form': AddTraineeform()})

    def post(self, request):
        # form = AddTraineeform(request.POST)
        # if form.is_valid():
        #     name = request.POST['name']
        #     bdate = request.POST['bdate']
        #     track_id = request.POST['track']
        #     track = Track.objects.get(pk=track_id)
        #     Trainee.objects.create(name=name, track=track, bdate=bdate)
        #     messages.success(request, f'Trainee {name} added successfully.')
        #     return HttpResponseRedirect('/trainee/')
        # else:
        #     return render(request, 'trainee/add.html', {'tracks': Track.objects.all(),
        #                                             'form': AddTraineeform(),
        #                                             'msg': form.errors})

        form = AddTraineeform(request.POST)  # Create a form instance with submitted data
        if form.is_valid():
            name = form.cleaned_data['name']
            track = form.cleaned_data['track']
            bdate = form.cleaned_data['bdate']
            track_id = request.POST['track']
            track = Track.objects.get(pk=track_id)
            Trainee.objects.create(name=name, track=track, bdate=bdate)

            if name:
                Trainee.objects.create(name=name, track=track, bdate=bdate)
                return HttpResponseRedirect('/trainee/')
            else:
                context = {'msg': 'You must enter the Trainee\'s name'}
        else:
            context = {'form': form}  # Send the form back with errors

        return render(request, 'trainee/add.html', context)
