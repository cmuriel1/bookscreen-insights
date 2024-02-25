from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login as user_login, logout as user_logout
from django.contrib import messages

from .forms import RegisterForm


def login(request):
    if request.method == "POST":
        query = request.POST["query"]
        password = request.POST["password"]

        get_query = User.objects.filter(
            Q(username__iexact=query) | Q(email__iexact=query)
        ).distinct()

        if not get_query.exists() and get_query.count() != 1:
            messages.error(request, "This User Doesn't Exist")
            return redirect("accounts:login")

        user = get_query.first()

        if not user.check_password(password):
            messages.error(request, "Wrong Password")
            return redirect("accounts:login")

        # You can use
        user_login(request, user)
        return redirect("products:home")

    context = {}
    return render(request, "accounts/login.html", context)


def logout(request):
    user_logout(request)
    messages.success(request, "Back Soon!")
    return redirect("accounts:login")


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        messages.success(
            request, f"You Can Login Now, {user.first_name} {user.last_name}"
        )
        return redirect("accounts:login")

    print(form.errors)
    context = {"form": form}
    return render(request, "accounts/register.html", context)
