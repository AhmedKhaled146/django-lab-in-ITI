from . import views
from django.urls import path


app_name = 'track'

urlpatterns = [
    path ('', views.index, name='index'),
    # path ('add/', views.insert, name='insert'),
    path ('add/', views.insert, name='insert'), # For model Form action to add new track

    path ('delete/<int:id>', views.delete, name='delete'),
    path ('update/<int:id>', views.update, name='update'),

]
