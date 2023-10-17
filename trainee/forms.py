# from django import forms
# from trainee.models import *
# from track.models import *



# class AddTraineeform(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter trainee name'}))
#     bdate = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
#     track = forms.ModelChoiceField(queryset=Track.objects.all())



# # from django import forms
# # from .models import Trainee
# # from track.models import Track


# # class TraineeForm(forms.Form):
# #     name = forms.CharField(label='Name', max_length=100)
# #     track = forms.ChoiceField(choices=[(tra.ID,tra.Name) for tra in Track.objects.all()])
# #     birthdate = forms.DateField(label='Birthdate', widget=forms.DateInput(attrs={'type': 'date'}))
