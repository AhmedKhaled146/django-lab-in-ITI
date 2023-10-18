from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path ('login/', views.login, name='login'),
    path ('signup/', views.signup, name='signup'),
    path ('profile/', views.profile, name='profile'),
    path('logout/', views.Logout, name="logout"),
    path ('profile/edit/', views.profile_edit, name='profile_edit'),


]
