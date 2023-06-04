from django.db import models
from academic.models import ClassRegistration
from student.models import EnrolledStudent
from employee.models import EmployeeInfo
from account.models import UserProfile

class AttendanceManager(models.Manager):
    def create_attendance(self, std_class, std_roll, period):
        std_cls = ClassRegistration.objects.get(name=std_class)
        std = EnrolledStudent.objects.get(student_id=std_roll, class_name=std_cls)
        std_att = StudentAttendance.objects.create(
            class_name=std_cls,
            student=std,
            period=period,
            status=1
        )
        return std_att

class Period(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentAttendance(models.Model):
    class_name = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    student = models.ForeignKey(EnrolledStudent, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'period', 'date']

    def __str__(self):
        return str(self.student.student.personal_info.name)


class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.employee.user.username)
