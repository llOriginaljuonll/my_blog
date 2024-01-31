from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog

        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'BLOG NAME',
                    'class': 'border-0 text-dark',
                    'style': 'font-size: 3rem; font-weight: 500;',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Write Your Story.',
                    'class': 'border-0 fs-5 text-secondary',
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