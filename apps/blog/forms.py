from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog

        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your blog name.',
                    'type': 'text'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Write your blog content.',
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