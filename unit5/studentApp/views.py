from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Department


def index(request):
    return render(request, "index.html")


def success(request):
    return render(request, "success.html")


def reg(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("success")
    return render(request, "registration.html", {"form": form})


def depart(request):
    departments = Department.objects.prefetch_related("teachers").order_by("name")
    return render(request, "depart.html", {"departments": departments})


def contact(request):
    return render(request, "contact.html")
