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
