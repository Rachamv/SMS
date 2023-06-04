from django.db import models
import random
from parent.models import Guardian, EmergencyDetails
from academic.models import Department, Grade, ClassInfo, Section, Session, Subject, GuideTeacher

class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student-photos/')
    blood_group_choices = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choices, max_length=5)
    date_of_birth = models.DateField()
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choices, max_length=10)
    phone_no = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    birth_certificate_no = models.IntegerField()
    religion_choices = (
        ('Islam', 'Islam'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    religion = models.CharField(choices=religion_choices, max_length=45)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StudentAddressInfo(models.Model):
    present_address = models.TextField()
    permanent_address = models.TextField()
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.present_address


class GuardianInfo(models.Model):
    guardian_name = models.ForeignKey(Guardian, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.guardian_name)


class PreviousAcademicInfo(models.Model):
    institute_name = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    group = models.CharField(max_length=45)
    passing_year = models.IntegerField()

    def __str__(self):
        return self.institute_name


class Certificate(models.Model):
    birth_certificate = models.FileField(upload_to='documents/', blank=True)
    release_letter = models.FileField(upload_to='documents/', blank=True)
    testimonial = models.FileField(upload_to='documents/', blank=True)
    other_certificate = models.FileField(upload_to='documents/', blank=True)


class AcademicInfo(models.Model):
    class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    registration_no = models.IntegerField(unique=True, default=random.randint(0, 999999))
    status_choices = (
        ('not_enroll', 'Not Enroll'),
        ('enrolled', 'Enrolled'),
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
        ('passed', 'Passed'),
    )
    status = models.CharField(choices=status_choices, default='not_enroll', max_length=15)
    personal_info = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, null=True)
    address_info = models.ForeignKey(StudentAddressInfo, on_delete=models.CASCADE, null=True)
    guardian_info = models.ForeignKey(GuardianInfo, on_delete=models.CASCADE, null=True)
    emergency_contact_info = models.ForeignKey(EmergencyDetails, on_delete=models.CASCADE, null=True)
    previous_academic_info = models.ForeignKey(PreviousAcademicInfo, on_delete=models.CASCADE, null=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.registration_no)


class ClassRegistration(models.Model):
    name = models.CharField(max_length=10, unique=True)
    department_choices = (
        ('general', 'General'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('humanities', 'Humanities'),
        ('N/A', 'N/A')
    )
    grade_choices = (
        ('grade 1', 'Grade 1'),
        ('grade 2', 'Grade 2'),
        ('grade 3', 'Grade 3'),
        ('grade 4', 'Grade 4'),
        ('grade 5', 'Grade 5'),
        ('grade 6', 'Grade 6'),
        ('grade 7', 'Grade 7'),
        ('grade 8', 'Grade 8'),
        ('grade 9', 'Grade 9'),
        ('grade 10', 'Grade 10'),
        ('grade 11', 'Grade 11'),
        ('grade 12', 'Grade 12'),
    )
    department = models.CharField(choices=department_choices, max_length=15)
    grade = models.CharField(choices=grade_choices, max_length=15)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    guide_teacher = models.ForeignKey(GuideTeacher, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name', 'section', 'guide_teacher']

    def __str__(self):
        return self.name



