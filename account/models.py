
from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher
from parent.models import Guardian
from administration.models import ChiefExecutive, Director, Secretary
from student.models import PersonalInformation
from datetime import date


class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField()
    role_choices = (
        ('admin', 'Admin'),
        ('director', 'Director'),
        ('register', 'Register'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    )
    role = models.CharField(choices=role_choices, max_length=15)

    def __str__(self):
        return self.name

@property
def age(self):
    today = date.today()
    age = today.year - self.date_of_birth.year
    if today.month < self.date_of_birth.month or (
        today.month == self.date_of_birth.month and today.day < self.date_of_birth.day
    ):
        age -= 1
    return age


@property
def age(self):
    return self.user_registration.age

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='photos/')
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6)
    employee_select = (
        ('admin', 'Admin'),
        ('director', 'Director'),
        ('register', 'Register'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    )
    employee_type = models.CharField(choices=employee_select, max_length=15)
    admin = models.OneToOneField(ChiefExecutive, on_delete=models.CASCADE, null=True, blank=True)
    director = models.OneToOneField(Director, on_delete=models.CASCADE, null=True, blank=True)
    register = models.OneToOneField(Secretary, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.OneToOneField(Guardian, on_delete=models.CASCADE, null=True, blank=True)
    student = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE, null=True, blank=True)
    registration = models.OneToOneField(UserRegistration, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def is_admin(self):
        return self.employee_type == 'admin'

    @property
    def is_director(self):
        return self.employee_type == 'director'

    @property
    def is_register(self):
        return self.employee_type == 'register'

    @property
    def is_teacher(self):
        return self.employee_type == 'teacher'

    @property
    def is_parent(self):
        return self.employee_type == 'parent'

    @property
    def is_student(self):
        return self.employee_type == 'student'
