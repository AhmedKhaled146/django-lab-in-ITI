from . import views
from django.urls import path
from trainee.views import *


app_name = 'trainee'

urlpatterns = [
    path ('', views.list, name='list'),
    # path ('add/', views.insert, name='insert'),
    path('insert',TraineeAdd.as_view(), name='insert'),
    path ('update/<int:id>/', views.update, name='update'),
    path ('delete/<int:id>/', views.delete, name='delete'),

]


