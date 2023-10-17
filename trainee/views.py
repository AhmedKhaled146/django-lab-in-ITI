from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
# from django.views.generic.edit import CreateView
from django.views import View
# from .forms import TraineeForm
# from django.urls import reverse_lazy
# Create your views here.




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
        return render(request, 'trainee/add.html', {'tracks': Track.objects.all()})

    def post(self, request):
        name = request.POST['name']
        bdate = request.POST['bdate']
        track_id = request.POST['track']
        track = Track.objects.get(pk=track_id)
        Trainee.objects.create(name=name, track=track, bdate=bdate)
        messages.success(request, f'Trainee {name} added successfully.')
        return HttpResponseRedirect('/trainee/')




# class TraineeInsertView(View):
#     template_name = 'trainee/insert.html'

#     def get(self, request):
#         # context = {}
#         # context['track'] = Track.objects.all()
#         # return render(request, self.template_name, context)
#         form = TraineeForm()
#         context = {'form': form}
#         return render(request, self.template_name, context)


#     def post(self, request):
#         # name = request.POST.get('name', '')
#         # track_id = request.POST.get('track_id', '')
#         # birthdate = request.POST.get('birthdate', '')

#         # if name:
#         #     Trainee.objects.create(Name=name, track=Track.objects.get(ID=track_id), BirthDate=birthdate)
#         #     return HttpResponseRedirect('/Trainee/List')
#         # else:
#         #     context = {'msg': 'You must enter the Trainee\'s name'}
#         #     return render(request, self.template_name, context)
#         form = TraineeForm(request.POST)  # Create a form instance with submitted data
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             track = form.cleaned_data['track']
#             birthdate = form.cleaned_data['birthdate']

#             if name:
#                 Trainee.objects.create(Name=name, track=Track.objects.get(ID=track), BirthDate=birthdate)
#                 return HttpResponseRedirect('/Trainee/List')
#             else:
#                 context = {'msg': 'You must enter the Trainee\'s name'}
#         else:
#             context = {'form': form}  # Send the form back with errors

#         return render(request, self.template_name, context)
