from django.contrib import messages
from django.shortcuts import render, redirect

from Users.forms import RegistrationForm, TeacherRegistrationForm, StudentRegistrationForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form': form})


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('teacher_register')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})


def accounts(request):
    return render(request, 'accounts.html')


def about(request):
    return render(request, 'about.html')


def assignment(request):
    return render(request, 'assignment.html')


def contact(request):
    return render(request, 'contact.html')


def exams(request):
    return render(request, 'exams.html')


def notes(request):
    return render(request, 'notes.html')


def resources(request):
    return render(request, 'resources.html')


def student_log_in(request):
    return render(request, 'student_log_in.html')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('student_register')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})


def student(request):
    return render(request, 'students.html')


def teacher(request):
    return render(request, 'teachers.html')


def teacher_log_in(request):
    return render(request, 'teacher_log_in.html')
