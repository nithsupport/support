from django.contrib.auth.forms import PasswordChangeForm
from support_app.models import User
from django import forms

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={'type': 'password', 'class':'form-control form-control-lg', 'id':'reset-password', 'placeholder': 'Current Password',}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'type': 'password', 'class':'form-control form-control-lg', 'id':'reset-newpassword', 'placeholder': 'New Password',}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'type': 'password', 'class':'form-control form-control-lg', 'id':'reset-confirmpassword', 'placeholder': 'Confirm Password',}))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']