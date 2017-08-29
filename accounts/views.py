from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def terms(request):
    return render(request, 'login.html', {})


@login_required(login_url='/users/login/')
def home(request):
    if request.user.is_staff:
        return redirect('/users/adminpanel/')
    return render(request, 'index.html', {})