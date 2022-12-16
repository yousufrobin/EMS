from django.shortcuts import render, HttpResponse
from app_EMS.models import Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "index.html")


def employee(request):
    emps = Employee.objects.all()
    context = {"emps": emps}
    return render(request, "employee.html", context)


def add_employee(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dept = request.POST.get("dept")
        role = request.POST.get("role")
        salary = request.POST.get("salary")
        bonus = request.POST.get("bonus")
        phone = request.POST.get("phone")

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date=datetime.now(),
        )
        new_emp.save()
        return HttpResponse("Employee Added!")
    elif request.method == "GET":
        return render(request, "add_employee.html")
    else:
        return HttpResponse("An Error Occured")
    return render(request, "add_employee.html")


def remove_employee(request, employee_id=0):
    if employee_id:
        try:
            employee_to_be_removed = Employee.objects.get(id=employee_id)
            employee_to_be_removed.delete()
            return HttpResponse(
                f"Janab {employee_to_be_removed.first_name} {employee_to_be_removed.last_name} is removed successfully."
            )
        except:
            return HttpResponse("Enter a Valid Employee ID!")

    emps = Employee.objects.all()
    context = {"emps": emps}
    return render(request, "remove_employee.html", context)


def search_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dept = request.POST.get("dept")
        role = request.POST.get("role")
        phone = request.POST.get("phone")
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        if phone:
            emps = emps.filter(phone__icontains=phone)

        context = {"emps": emps}
        return render(request, "employee.html", context)

    elif request.method == "GET":
        return render(request, "search_employee.html")
    else:
        return HttpResponse("An Exception Occurred")
