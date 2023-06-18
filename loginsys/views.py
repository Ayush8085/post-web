from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'index.html')

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("ERROR")


    return render(request, 'loginsys/login.html')

def registerUser(request):

    form = RegisterForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Sending welcome mail
            subject = 'Welcome to SymDa'
            message = 'We are glad that you are here.'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )

            return redirect('home')

    context = {'form': form}
    return render(request, 'loginsys/registerUser.html', context)
