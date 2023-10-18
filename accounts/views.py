from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.



def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created successfully for " + user)
            user = authenticate(request, user=user)
            # login(request, user)
            return redirect('accounts:profile')
    else:
        form = SignupForm()

    context = {'form': form,
               'title': "register",}
    return render(request, 'registration/signup.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
    return render(request, 'registration/login.html')


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})



@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,instance=profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)


    return render(request, 'registration/profile_edit.html', {'userform': userform,
                                                              'profileform': profileform})


@login_required
def Logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
