from django import forms
from .models import Image


class CreateImageForm(forms.ModelForm):
    class Meta:

        model=Image

        fields = ['title','description','url']

        widgets={
            'url': forms.HiddenInput,
        }
