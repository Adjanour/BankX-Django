from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class DepositForm(forms.Form):
    amount = forms.DecimalField(
        label='Amount to Deposit',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0.01,  # Set a minimum deposit amount
        required=True
    )
    pin = forms.CharField(
        label='PIN',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=4,  # Set a minimum PIN length
        max_length=4,  # Set a maximum PIN length
        required=True
    )

class WithdrawalForm(forms.Form):
    amount = forms.DecimalField(
        label='Amount to Withdraw',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0.01,  # Set a minimum withdrawal amount
        required=True
    )
    pin = forms.CharField(
        label='PIN',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=4,  # Set a minimum PIN length
        max_length=4,  # Set a maximum PIN length
        required=True
    )