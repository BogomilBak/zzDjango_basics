from random import choice
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect, render

# def show_departments(request: HttpRequest, *args, **kwarags):
#     print(request.method)
#     print(request.GET)
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#     body = f'path: {request.path}args={args}, kwargs={kwarags}'
#     return HttpResponse(body)

def show_departments(request: HttpRequest, *args, **kwarags):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }
    return render(request, 'departments/all.html', context)

def show_departments_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)

def show_department_by_id(request, department_id):
    if department_id == 1:
        department_name = "Developers"
    elif department_id == 2:
        department_name = "Trainers"
    html = "<html><body><h1>" \
    "Department Name: %s, Department ID: %s" \
    "</h1></body></html>" \
    % (department_name, department_id)
    return HttpResponse(html)

def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # to = f'/departments/?order_by={order_by}'
    # to = 'http://softuni.bg'
    return redirect('show department details', department_id=13)

def show_not_found(request):
    status_code = 404
    # return HttpResponse('error', status=status_code)
    raise Http404('not found')
