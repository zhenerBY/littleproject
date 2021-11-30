from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from main.models import AdvUser


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (repeat)',
                                widget=forms.PasswordInput,
                                help_text='Enter the same password again for verification')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'The passwords entered do not match', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name',)