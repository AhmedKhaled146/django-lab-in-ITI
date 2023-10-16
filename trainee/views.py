from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trainee
from .models import *
# from .models import Trainee, Track
from django.contrib import messages
# from django.views.generic.edit import CreateView
from django.views import View
# from .forms import TraineeForm
# from django.urls import reverse_lazy
# Create your views here.




def list(request):
    all_trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'all_trainees': all_trainees})


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


# from django.shortcuts import render
# from django.http.response import HttpResponse,HttpResponseRedirect
# from django.views import View
from .forms import *
# from .models import *


class TraineeAdd(View):
    def get(self,req):
        context = {}
        context['track'] = Track.objects.all()
        context['form']=AddTraineeform()
        return render(req, 'trainee/add.html', context)

    def post(self,req):
        form=AddTraineeform(req.POST)
        if(form.is_valid()):
            name = req.POST['name']
            track_id = req.POST['track']
            Trainee.objects.create(name=name, track=Track.objects.get(id=track_id),bdate=req.POST['bdate'])
            return HttpResponseRedirect('List')
        else:
            context={'MSG':form.errors}
            return render(req, 'trainee/add.html', context)

# class TraineeDelete(View):
#     def get(self, req, id):
#         Trainee.objects.filter(id=id).delete()
#         return HttpResponseRedirect('List')

# # Create your views here.
# def traineelist(req):
#     context = {}
#     trainees = Trainee.objects.all()
#     context['trainees'] = trainees
#     return render (req,'trainee/list.html',context)

# def traineeupdate(req,id):
#     context = {}
#     context['track'] = Track.objects.all()
#     context['oldTraineeData'] = Trainee.objects.get(id=id)
#     if (req.method == 'POST'):
#         Trainee.objects.filter(id=id).update(name=req.POST['name'], bdate=req.POST['DOB'],
#                                              track=Track.objects.get(id=req.POST['track']))
#     return render(req,'trainee/update.html',context)

