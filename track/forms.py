from django import forms
from .models import *


class AddNewTrack(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
