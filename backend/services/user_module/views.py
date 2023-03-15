from django.shortcuts import render, redirect

from django.http import HttpResponseNotFound

from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login

from services.user_module.forms import RegistrationForm, AuthForm, ProfileForm

from settings import SITE_URL

from django.contrib.auth.hashers import make_password

User = get_user_model()


def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.data['email'],
                                            username=form.data['username'],
                                            password=form.data['password'])

            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']

            user.save()

            return redirect('index')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', context={'form': form})


def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        user = authenticate(username=form.data['username'],
                            password=form.data['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthForm()

            return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL})
    else:
        form = AuthForm()

    return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')

    if not request.user.is_seller:
        return HttpResponseNotFound

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user

            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']

            if not User.objects.filter(email=form.data['email']).exists():
                user.email = form.data['email']

            if not User.objects.filter(username=form.data['username']).exists():
                user.username = form.data['username']

            if form.data['password_old'] and form.data['password_new'] and user.check_password(form.data['password_old']):
                user.password = make_password(form.data['password_new'])

            user.save()

            return redirect('profile')
        else:
            return render(request, 'registration.html', context={'form': form})

    else:
        form = ProfileForm(data={'first_name': request.user.first_name,
                                 'last_name': request.user.last_name,
                                 'username': request.user.username,
                                 'email': request.user.email})

        return render(request, 'profile.html', context={'form': form})

