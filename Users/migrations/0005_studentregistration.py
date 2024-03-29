# Generated by Django 5.0.3 on 2024-03-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_teacherregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=15)),
                ('admission_number', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('father_name', models.CharField(max_length=20)),
                ('father_phone', models.CharField(max_length=10)),
                ('mother_name', models.CharField(max_length=20)),
                ('mother_phone', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('religion', models.CharField(choices=[('Christian', 'Christian'), ('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha')], default='', max_length=10)),
                ('other_religion', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=10)),
            ],
        ),
    ]
