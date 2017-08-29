from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input input-material'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input input-material'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Username',
            'email': 'E-mail',
            'password': 'Password',
            'password2': 'Confirm Password'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input input-material', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input input-material', 'required': True})
        }

    #Validation password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")
        return cd['password2']
    #validation e-mail
    def clean_email(self):
        email= self.cleaned_data.get('email')
        print(User.objects.filter(email=email).count())
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input input-material', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input-material', 'placeholder': 'Password'}))
