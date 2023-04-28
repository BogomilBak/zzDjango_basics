from django.urls import path
from departments.views import *


urlpatterns = [
    path('', show_departments),
    path('<department_id>', show_departments_details),
    path('int/<int:department_id>/', show_departments_details),
]
