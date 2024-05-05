from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog

        exclude = ('likes',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'HEAD!',
                    'class': 'text-dark focus:outline-none py-2 container mx-auto text-5xl font-medium',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'WRITE YOUR STORY . . . .',
                    'class': 'border-0 container focus:outline-none text-xl',
                }
            ),
            'writer': forms.TextInput(
                attrs={
                    'value': '',
                    'id': 'writer',
                    'type': 'hidden'
                }
            )
        }

        labels = {
            'name': '',
            'body': '',
        }