from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Настройка поля username
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Логин',
            'autocomplete': 'username'
        })

        # Настройка поля password1
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль',
            'autocomplete': 'new-password'
        })

        # Настройка поля password2
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
            'autocomplete': 'new-password'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)