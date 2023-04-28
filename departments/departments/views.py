from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def show_departments(request: HttpRequest, *args, **kwarags):
    print(request.method)
    print(request.GET)
    print(request.get_port())
    print(request.get_host())
    print(request.headers)
    body = f'path: {request.path}args={args}, kwargs={kwarags}'
    return HttpResponse(body)

def show_departments_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)
