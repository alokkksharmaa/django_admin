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


def delete(request):
    response = HttpResponse("Cookie deleted successfully")
    response.delete_cookie("username")
    return response


def visit_again(request):
    value = int(request.COOKIES.get("visit"))
    value+=1
    response=HttpResponse()
    response.set_cookie("Visit", value, max_age=3600)
    return HttpResponse(f"total visits: " {value})
    return response

