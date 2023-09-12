from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Account 


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('account_overview')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




def index(request):
    return render(request, 'index.html')



@login_required
def account_overview(request):
    user = request.user
    account = Account.objects.get(user=user)
    context = {'user': user, 'account': account}
    return render(request, 'account_overview.html', context)

@login_required
def deposit(request):
    if request.method == 'POST':
        # Handle deposit logic here (update account balance)
        return redirect('account_overview')
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        # Handle withdrawal logic here (update account balance)
        return redirect('account_overview')
    return render(request, 'withdraw.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Handle account deletion logic here
        return redirect('logout')  # Redirect to logout page after deleting the account
    return render(request, 'delete_account.html')
