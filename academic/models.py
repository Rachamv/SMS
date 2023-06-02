from django.db import models
from teacher.models import PersonalInfo

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=10, unique=True)
    display_name = models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name


class ClassInfo(models.Model):
    name = models.CharField(max_length=45, unique=True)
    display_name = models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name

class Section(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.IntegerField(unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class GuideTeacher(models.Model):
    name = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class ClassRegistration(models.Model):
    name = models.CharField(max_length=10, unique=True)
    department_select = (
        ('general', 'General'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('humanities', 'Humanities')
    )
    grade_select = (
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
    department = models.CharField(choices=department_select, max_length=15)
    grade = models.CharField(choices=grade_select, max_length=15)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    guide_teacher = models.ForeignKey(GuideTeacher, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name', 'section', 'guide_teacher']

    def __str__(self):
        return self.name
