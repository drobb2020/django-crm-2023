from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from core.forms import SignupForm
from core.models import Record


def index(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("index")
        else:
            messages.success(request, "OOPS! Something went wrong, please try again.")
            return redirect("index")
    else:
        context = {'records': records}
        return render(request, "core/index.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out...")
    return redirect("index")


def register_user(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You have successfully registered and logged in. Welcome!"
            )
            return redirect("index")
    else:
        context = {"form": form}
        return render(request, "core/register.html", context)

    context = {"form": form}
    return render(request, "core/register.html", context)
