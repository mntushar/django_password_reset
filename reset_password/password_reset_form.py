from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label= "Email Address",
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'required':'True'})
    )


class AccountSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'required':'True'}),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'required': 'True'}),
    )