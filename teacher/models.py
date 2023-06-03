from django.db import models
from employee.models import Employee
from academic.models import ClassInfo, Subject, Grade
from student.models import Student
from attendance.models import StudentAttendance


class Teacher(Employee):
    teacher_id = models.CharField(max_length=20, unique=True)
    specializations = models.CharField(max_length=100)
    teaching_assignments = models.ManyToManyField(Grade, through='TeachingAssignment')

    def give_special_report(self, student, report):
        special_report = SpecialReport.objects.create(teacher=self, student=student, report=report)
        return special_report

    def mark_attendance(self, class_instance, date, status, remarks=None):
        attendance = Attendance.objects.create(teacher=self, class_instance=class_instance, date=date, status=status, remarks=remarks)
        return attendance


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject_assigned = models.ForeignKey(Subject, on_delete=models.CASCADE)


class SpecialReport(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_instance = models.ForeignKey(Grade, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)
    remarks = models.CharField(max_length=255, blank=True, null=True)


class Test(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_instance = models.ForeignKey(Grade, on_delete=models.CASCADE)
    date = models.DateField()
    max_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()


class Exam(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_instance = models.ForeignKey(Grade, on_delete=models.CASCADE)
    date = models.DateField()
    max_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)


class LessonPlan(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_instance = models.ForeignKey(Grade, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
