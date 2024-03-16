from django import forms

from Users.models import Registration


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password', 'gender']
