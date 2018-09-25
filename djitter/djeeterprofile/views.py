from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from djeeterprofile.forms import SignupForm, SigninForm


def frontpage(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')

            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')

        else:
            signupform = SignupForm()
            signinform = SigninForm()

    return render(request, 'frontpage.html', {'signupform': signupform,
                                              'signinform': signinform})


def signout(request):
    logout(request)
    return redirect('/')


def profile(request, username):
    user = User.objects.get(username=username)

    return render(request, 'profile.html', {'user': user})
