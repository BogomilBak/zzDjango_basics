from django.db import models
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(
        max_length=15,
    )

    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'Id: {self.pk}; Name{self.name}'
    
    def get_absolute_url(self):
        return reverse("details department", kwargs={"pk": self.pk})
    
    
    
class Project(models.Model):
    name = models.CharField(
        max_length=30,
        )
    code_name = models.CharField(
        max_length=10,
        unique=True,
        )
    deadline = models.DateField()

class Employee(models.Model):

    class Meta:
        ordering = ['age']

    first_name = models.CharField(
        max_length=40,
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
    )
    start_date = models.DateField()
    years_of_experience = models.PositiveIntegerField(
        null=True,
    ) 

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    project = models.ManyToManyField(
        Project,
        related_name='employees',
        )

    # this will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # this will be automaticall set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    level = models.CharField(
        max_length=25,
        choices=(
            ('jr', 'Junior'),
            ('reg', 'Regular'),
            ('sr', 'Senior'),
        ),
        verbose_name='Seniority level',
    )

    email = models.EmailField(
        unique=True,
    )
    works_full_time = models.BooleanField()
    photo = models.URLField()
    age = models.IntegerField(
        default=-18,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name:{self.fullname}'
    
class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,
        null=True,
    ) 
    default = models.IntegerField(
        blank=False,
        null=False,
    )

class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
        )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
        )

    date_joined = models.DateField(
        auto_now=True,
    )

class AcessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True, 
    )

class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )