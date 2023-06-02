from django.db import models
from django.contrib.auth.models import User
from academic.models import Department
from address.models import Address

class EducationInfo(models.Model):
    # Existing fields

    LEVEL_CHOICES = (
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('higher-secondary', 'Higher Secondary'),
        ('bachelors', 'Bachelors'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
        ('other', 'Other'),
    )

    name_of_exam = models.CharField(max_length=100)
    institute = models.CharField(max_length=255)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    major = models.CharField(max_length=100)
    result = models.CharField(max_length=45)
    passing_year = models.IntegerField()
    certificate = models.FileField(upload_to='employee_documents/', blank=True, null=True)

    def __str__(self):
        return self.name_of_exam

class TrainingInfo(models.Model):
    # Existing fields

    training_name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    duration_in_hours = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.training_name

class EmployeeJobInfo(models.Model):
    # Existing fields

    EMPLOYEE_CATEGORIES = (
        ('teaching', 'Teaching Staff'),
        ('non-teaching', 'Non-Teaching Staff'),
        ('head-teacher', 'Head Teacher'),
        ('secretary', 'Secretary'),
    )

    DESIGNATION_LEVELS = (
        ('level1', 'Level 1'),
        ('level2', 'Level 2'),
        ('level3', 'Level 3'),
        ('level4', 'Level 4'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=EMPLOYEE_CATEGORIES)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation_level = models.CharField(max_length=10, choices=DESIGNATION_LEVELS)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.designation

class ExperienceInfo(models.Model):
    # Existing fields

    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    trainings = models.ManyToManyField(TrainingInfo, blank=True)

    def __str__(self):
        return self.organization

class PersonalInfo(models.Model):
    # Existing fields

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    BLOOD_GROUP_CHOICES = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-'),
    )

    MARITAL_STATUS_CHOICES = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single'),
    )

    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='photos/')
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    nationality = models.CharField(max_length=45)
    religion = models.CharField(max_length=45)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    e_tin = models.CharField(max_length=11, unique=True)  # Employee Tax Identification Number
    nid = models.CharField(max_length=11, unique=True)  # National Identification Number
    driving_license_passport = models.CharField(max_length=11, unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='employee_documents/', blank=True, null=True)  # Updated upload_to value
    father_name = models.CharField(max_length=45)
    mother_name = models.CharField(max_length=45)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    emergency_contact = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    # Existing fields

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    employee = models.ForeignKey(EmployeeJobInfo, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}"

class EmployeeDocument(models.Model):
    # Existing fields

    employee = models.ForeignKey(EmployeeJobInfo, on_delete=models.CASCADE)
    document = models.FileField(upload_to='employee_documents/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.document.name}"
