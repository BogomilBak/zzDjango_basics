from django.urls import path
from departments.views import *


urlpatterns = [
    path('', show_departments, name='show departments'),
    path('<department_id>', show_departments_details, name='show department details'),
    path('department/<int:department_id>/', show_department_by_id,),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('not-found/', show_not_found, name='not found'),
]
