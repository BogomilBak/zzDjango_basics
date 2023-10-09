from django.shortcuts import get_object_or_404, render

from web.models import Department, Employee

from django.contrib.auth.models import User

def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(years_of_experience=26)
    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)

def department_details(request, pk):
    context = {
        'department': get_object_or_404(Department, pk=pk)
    }
    return render(request, 'department-details.html', context)