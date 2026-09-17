import re

from django.http import HttpResponse
STUDENT_ID_PATTERN = re.compile(r"^CSE\d{4}[A-Z]\d{3}$")

def result(request, student_id, marks):
    if int(marks) >= 75:
        division = "Distinction"
    else:
        if int(marks) >= 60:
            division = "First Division"
        else:
            if int(marks) >= 40:
                division = "Second Division"
            else:
                division = "Fail"





    return HttpResponse(
        f"Student ID: {student_id}, Marks: {marks}, Result: {division}",
        status=200,
    )
