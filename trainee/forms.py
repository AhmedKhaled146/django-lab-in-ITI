from django import forms
from django.core.exceptions import ValidationError
from trainee.models import Trainee
from track.models import Track
from datetime import date


class AddTraineeform(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    bdate = forms.DateField(input_formats=['%Y-%d-%m'], help_text='YYYY-14-01')
    track = forms.ModelChoiceField(queryset=Track.objects.all())
