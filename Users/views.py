from django.contrib import messages
from django.shortcuts import render, redirect

from Users.forms import RegistrationForm


# Create your views here.


def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form': form})

