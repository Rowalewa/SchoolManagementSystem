"""
URL configuration for SchoolManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('accounts/', views.accounts, name='accounts'),
    path('teacherregistration/', views.teacher_register, name='teacher_register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('assignment/', views.assignment, name='assignment'),
    path('exams/', views.exams, name='exams'),
    path('notes/', views.notes, name='notes'),
    path('resources/', views.resources, name='resources'),
    path('studentlogin/', views.student_log_in, name='student_login'),
    path('studentregister/', views.student_register, name='student_register'),
    path('teacherlogin/', views.teacher_log_in, name='teacher_login'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student')

]
