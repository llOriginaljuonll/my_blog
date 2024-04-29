from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)

        self.fields['username'].label = 'Username'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['password1'].label = 'Password'

        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password1'].help_text = None



