from django import forms
from . models import profile


class ProfileForm(forms.ModelForm):
    Email = forms.EmailField(max_length=30)

    class Meta():
        model=profile
        fields=('Email',)
