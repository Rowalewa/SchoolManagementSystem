from django.db import models


# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')

    def __str__(self):
        return self.first_name


class TeacherRegistration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)
    teacher_service_number = models.CharField(max_length=8)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    MARRIAGE_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced')
    )
    marriage_status = models.CharField(max_length=10, choices=MARRIAGE_CHOICES, default='Single')

    def __str__(self):
        return self.first_name


class StudentRegistration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=5)
    email = models.EmailField()
    father_name = models.CharField(max_length=20)
    father_phone = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=20)
    mother_phone = models.CharField(max_length=10)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    RELIGION_CHOICES = (
        ('Christian', 'Christian'),
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Buddha', 'Buddha')
    )
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, default='')
    other_religion = models.CharField(max_length=20)
    nationality = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
