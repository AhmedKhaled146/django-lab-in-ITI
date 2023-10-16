from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Instructor
# Create your views here.

def index(request):
    all_instructor = Instructor.objects.all()
    messages_list = messages.get_messages(request)
    context = {'all_instructor': all_instructor, 'messages': messages_list}
    # print(all_instructor)

    return render(request, 'instructor/list.html', context)

def insert(request):
    if request.method == 'POST':
        instructor_name = request.POST.get('name', None)
        salary = request.POST.get('salary', None)
        instructor_date = request.POST.get('bdate', None)

        if instructor_name and salary and instructor_date:
            response = Instructor(
                name=instructor_name,
                salary=salary,
                bdate=instructor_date
            )
            response.save()
            messages.success(request, f'Instructor {instructor_name}added successfully.')
            return HttpResponseRedirect('/instructor/')  # Redirect to the index page
        else:
            messages.error(request, 'All fields (Name, Salary, and Instructor Date) are required')

    return render(request, 'instructor/add.html')

def delete(request, id):
    Instructor.objects.filter(id=id).delete()
    return HttpResponseRedirect('/instructor/') # Redirect to the index page

def update(request, id):
    instructor = get_object_or_404(Instructor, pk=id)
    if request.method == 'POST':
        instructor.name = request.POST['name']
        instructor.salary = request.POST['salary']
        instructor.bdate = request.POST['bdate']
        instructor.save()
        return HttpResponseRedirect('/instructor/') # Redirect to the index page
    return render(request, 'instructor/update.html', {'instructor': instructor})
