from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from core.forms import CreateUser, SignupForm
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
        context = {"records": records}
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


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        context = {"record": customer_record}
        return render(request, "core/record.html", context)
    else:
        messages.success(request, "You must be logged in to view a customer record.")
        return redirect("index")


def create_record(request):
    form = CreateUser(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "New customer record added successfully.")
                return redirect("index")
        context = {'form': form}
        return render(request, "core/create.html", context)
    else:
        messages.success(request, "You must be logged in to create a record.")
        return redirect("index")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = CreateUser(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer record updated successfully.")
            return redirect("index")
        context = {'form': form}
        return render(request, "core/update.html", context)
    else:
        messages.success(request, "You must be logged in to update a record.")
        return redirect("index")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record successfully deleted.")
        return redirect("index")
    else:
        messages.success(request, "You must be logged in to delete a record.")
        return redirect("index")
