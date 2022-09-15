from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def account(request):
    if request.method == "GET":
        return render(request, 'account/home.html')

def login_view(request):
    if request.method == "GET":
        return render(request, 'account/login.html')
    if request.method == "POST":
        data = request.POST
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'account/home.html')

def logout_view(request):
    if str(request.user) != "AnonymousUser":
        if request.method == "GET":
            logout(request)
            return render(request, 'account/home.html')
    else:
        return redirect("account:login")