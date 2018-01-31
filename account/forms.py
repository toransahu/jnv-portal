from django import forms


class CreateForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
