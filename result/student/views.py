import re

from django.http import HttpResponse

def result(request, student_id, marks):
    if int(marks) >= 75:
        return HttpResponse("Distinction")
    else:
        if int(marks) >= 60:
            return HttpResponse("First Division")
        else:
            if int(marks) >= 40:
                return HttpResponse("Second Division")
            else:
                return HttpResponse("Fail")
