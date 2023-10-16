from django import forms
from trainee.models import *
from track.models import *




class AddTraineeform(forms.Form):
    name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'placeholder':'enter trainee name'}))
    bdate = forms.DateTimeField(label='DateOfBirth', widget=forms.DateInput(attrs={'type':'date'}))
    track = forms.ChoiceField(choices=[(track.id,track.name) for track in Track.objects.all()])
