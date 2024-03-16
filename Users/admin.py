from django.contrib import admin

from Users.models import Registration, TeacherRegistration, StudentRegistration

# Register your models here.
admin.site.register(Registration)
admin.site.register(TeacherRegistration)
admin.site.register(StudentRegistration)
