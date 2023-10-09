from django.contrib import admin

from web.models import Category, Department, Employee, NullBlankDemo, Project

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass