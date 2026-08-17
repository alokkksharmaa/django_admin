from django.http import HttpResponse
import math

def index(request):
    return HttpResponse("Hello, world. Welcome to my Django project!")

def student(req):
    return HttpResponse("<h1>Welcome to the student page!</h1>")

def teacher(req):
    return HttpResponse("<h1> Welcome to the teacher page </h1>")


def student1(request):
    name="Alok"
    course="django"
    return HttpResponse(f" <h1>My name  {name} is and my course  is: {course} </h1> ")


def check(request):
    num = 10
    if num % 2 == 0:
        return HttpResponse(f" <h1>number is {num} Even</h1> ")
    else:
        return HttpResponse(f" <h1>Number is {num} odd</h1> ")

def course(request, course_name):
    return HttpResponse(f"<h1>Welcome to the {course_name} course page!</h1>")

def emp(request, emp_id, emp_name):
    employee = {
        "emp_id": emp_id,
        "emp_name": emp_name
    }
    return HttpResponse(f"<h1>Employee ID: {employee['emp_id']},<br>Employee Name: {employee['emp_name']}</h1>")

def website1(request, id):
    return HttpResponse(f"Welcome to the website page of {id}")

def website2(request, id):
    return HttpResponse(f"Welcome to the website page of {id}")


def about(request):
    return HttpResponse("Welcome to About")

# Query Parameter 
def blog(request):
    data = request.GET.get("id")
    return HttpResponse(f"this is my Blog: {data} page")

def blog1(request, id):
    return HttpResponse(f"this is my Blog1 {id} page")

# query parameter
def profile(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    salary = request.GET.get("salary")
    return HttpResponse(f""" <h1> Employee details: </h1>
                         <h3>Name: {name}  <br>
                        id: {id} 
                        <br> 
                        salary:  {salary}  </h3>""")



#  ===========ERROR Handling==========
# types -- 
# status codes
#  200 - OK
# 201 -> created
# 400 -> bad request
# 403 ->  forbidden
# 404 -> not found
# 500 -> internal server 

def studentinfo(request):
    id=request.GET.get("id")

    if id is None:
        return HttpResponse("id is required", status=400)
    else:
        return HttpResponse(f"Student id is: {id}")
# http://127.0.0.1:8000/student/?id=12

def sum(request):
    num1=float(request.GET.get("num1"))
    num2=float(request.GET.get("num2"))
    try:
        result = float(num1)/float(num2)
        return HttpResponse(f"Result is: {result}")
    except ZeroDivisionError:
        return HttpResponse("zero division error")
    except ValueError:
        return HttpResponse("value error : enter only numbers")
    finally:
        return HttpResponse("code done")