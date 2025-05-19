from django.shortcuts import render, HttpResponse,redirect
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, "index.html")

def all_employ(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }

    return render(request, "all_employ.html", context)

def add_employ(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        role_id = request.POST.get('role')
        dept_id = request.POST.get('dept')
        location = request.POST.get('location')

        insertquery = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, role=Role(id=role_id), dept=Department(id=dept_id), location=location, hire_date=datetime.now())

        insertquery.save()
        return HttpResponse("Employee Add Successfully")

    return render(request, "add_employ.html")

def remove_employ(request):
    emps = Employee.objects.all()
    context = {
        'emp': emps,
    }
    return render(request, "remove_employ.html", context)

def remove_emp(request,emp_id):
    emp_remove = Employee.objects.get(id=emp_id).delete()
    return HttpResponse("Employee Remove successfully")
    return redirect("/remove_employ")

def filter_employ(request):
    if request.method == "POST":
        name = request.POST.get('name')
        role = request.POST.get('role')
        dept = request.POST.get('dept')

        emps = Employee.objects.all()

        if name:
          emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if role:
            emps = emps.filter(role__name__icontains= role)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        context = {
             'emps' : emps
        }
        return render(request,"all_employ.html",context)
    elif request.method == "GET":
        return render(request, "filter_employ.html")
    else:
        return HttpResponse("En Exeption error")

