from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'useraccounts/signup.html',
                              {'error': 'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                login(request, user)
                return render(request, 'useraccounts/signup.html')
        else:
            return render(request, 'useraccounts/signup.html',
                          {'error': 'Passwords didn\'t match!'})
    else:
        return render(request, 'useraccounts/signup.html')

def userlogin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return render(request, 'useraccounts/login.html',
                          {'error': 'Username and password didn\'t match!'})
    else:
        return render(request, 'useraccounts/login.html')

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
