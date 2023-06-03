from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Teacher, TeachingAssignment, SpecialReport, Attendance, Test, Exam, TestResult, ExamResult, LessonPlan
from academic.models import Grade, Subject, ClassInfo
from student.models import Student
from attendance.models import StudentAttendance 
from .forms import LessonPlanForm, SpecialReportForm, AttendanceForm, TestForm, ExamResultForm, TestResultForm, ExamForm
from .utils import calculate_grade

class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        teaching_assignments = teacher.teaching_assignments.all()
        special_reports = teacher.special_reports.all()
        attendance = teacher.attendance.all()
        tests = teacher.tests.all()
        exams = teacher.exams.all()
        lesson_plans = teacher.lesson_plans.all()

        context = {
            'teacher': teacher,
            'teaching_assignments': teaching_assignments,
            'special_reports': special_reports,
            'attendance': attendance,
            'tests': tests,
            'exams': exams,
            'lesson_plans': lesson_plans,
        }

        return render(request, 'teacher/teacher_detail.html', context)


class SpecialReportCreateView(View):
    def post(self, request, teacher_id, student_id):
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        student = get_object_or_404(Student, id=student_id)
        report = request.POST.get('report')

        if report:
            special_report = SpecialReport.objects.create(teacher=teacher, student=student, report=report)
            return redirect('teacher-detail', teacher_id=teacher.teacher_id)

        return redirect('teacher-detail', teacher_id=teacher.teacher_id)


class AttendanceCreateView(View):
    def post(self, request, teacher_id, class_id):
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        class_instance = get_object_or_404(Grade, id=class_id)
        date = request.POST.get('date')
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')

        if date and status:
            attendance = Attendance.objects.create(teacher=teacher, class_instance=class_instance,
                                                   date=date, status=status, remarks=remarks)
            return redirect('teacher-detail', teacher_id=teacher.teacher_id)

        return redirect('teacher-detail', teacher_id=teacher.teacher_id)


class TestCreateView(View):
    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        subject_id = request.POST.get('subject')
        class_id = request.POST.get('class')
        date = request.POST.get('date')
        max_marks = request.POST.get('max_marks')
        passing_marks = request.POST.get('passing_marks')

        if subject_id and class_id and date and max_marks and passing_marks:
            subject = get_object_or_404(Subject, id=subject_id)
            class_instance = get_object_or_404(Grade, id=class_id)
            test = Test.objects.create(teacher=teacher, subject=subject, class_instance=class_instance,
                                       date=date, max_marks=max_marks, passing_marks=passing_marks)
            return redirect('teacher-detail', teacher_id=teacher.teacher_id)

        return redirect('teacher-detail', teacher_id=teacher.teacher_id)


class ExamCreateView(View):
    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        subject_id = request.POST.get('subject')
        class_id = request.POST.get('class')
        date = request.POST.get('date')
        max_marks = request.POST.get('max_marks')
        passing_marks = request.POST.get('passing_marks')

        if subject_id and class_id and date and max_marks and passing_marks:
            subject = get_object_or_404(Subject, id=subject_id)
            class_instance = get_object_or_404(Grade, id=class_id)
            exam = Exam.objects.create(teacher=teacher, subject=subject, class_instance=class_instance,
                                       date=date, max_marks=max_marks, passing_marks=passing_marks)
            return redirect('teacher-detail', teacher_id=teacher.teacher_id)

        return redirect('teacher-detail', teacher_id=teacher.teacher_id)


class TestResultCreateView(View):
    def post(self, request, test_id, student_id):
        test = get_object_or_404(Test, id=test_id)
        student = get_object_or_404(Student, id=student_id)
        marks_obtained = request.POST.get('marks_obtained')
        
        if marks_obtained:
            marks_obtained = int(marks_obtained)
            grade = calculate_grade(marks_obtained)  # Calculate the grade based on marks obtained
            test_result = TestResult.objects.create(test=test, student=student, marks_obtained=marks_obtained, grade=grade)
            return redirect('teacher_detail', teacher_id=test.teacher.teacher_id)
        
        return redirect('teacher_detail', teacher_id=test.teacher.teacher_id)


class ExamResultCreateView(View):
    def post(self, request, exam_id, student_id):
        exam = get_object_or_404(Exam, id=exam_id)
        student = get_object_or_404(Student, id=student_id)
        marks_obtained = request.POST.get('marks_obtained')
        
        if marks_obtained:
            marks_obtained = int(marks_obtained)
            grade = calculate_grade(marks_obtained)  # Calculate the grade based on marks obtained
            exam_result = ExamResult.objects.create(exam=exam, student=student, marks_obtained=marks_obtained, grade=grade)
            return redirect('teacher_detail', teacher_id=exam.teacher.teacher_id)
        
        return redirect('teacher_detail', teacher_id=exam.teacher.teacher_id)


def mark_attendance(request, class_instance_id):
    class_instance = get_object_or_404(Grade, id=class_instance_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')

        teacher = get_object_or_404(Teacher, user=request.user)
        attendance = StudentAttendance.objects.create(class_instance=class_instance, teacher=teacher,
                                                      date=date, status=status, remarks=remarks)

        # Redirect to the attendance detail page or any other desired view
        return redirect('attendance-detail', attendance_id=attendance.id)

    context = {
        'class_instance': class_instance,
    }
    return render(request, 'teacher/mark_attendance.html', context)


def give_special_report(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        report = request.POST.get('report')

        teacher = get_object_or_404(Teacher, user=request.user)
        special_report = SpecialReport.objects.create(teacher=teacher, student=student, report=report)

        # Redirect to the special report detail page or any other desired view
        return redirect('special-report-detail', report_id=special_report.id)

    context = {
        'student': student,
    }
    return render(request, 'teacher/give_special_report.html', context)


class LessonPlanCreateView(View):
    def get(self, request):
        form = LessonPlanForm()
        return render(request, 'teacher/lessonplan_create.html', {'form': form})

    def post(self, request):
        form = LessonPlanForm(request.POST)
        if form.is_valid():
            lesson_plan = form.save()
            return redirect('lessonplan_detail', lessonplan_id=lesson_plan.id)
        return render(request, 'teacher/lessonplan_create.html', {'form': form})


class LessonPlanUpdateView(View):
    def get(self, request, lessonplan_id):
        lesson_plan = get_object_or_404(LessonPlan, id=lessonplan_id)
        form = LessonPlanForm(instance=lesson_plan)
        return render(request, 'teacher/lessonplan_update.html', {'form': form, 'lesson_plan': lesson_plan})

    def post(self, request, lessonplan_id):
        lesson_plan = get_object_or_404(LessonPlan, id=lessonplan_id)
        form = LessonPlanForm(request.POST, instance=lesson_plan)
        if form.is_valid():
            lesson_plan = form.save()
            return redirect('lessonplan_detail', lessonplan_id=lesson_plan.id)
        return render(request, 'teacher/lessonplan_update.html', {'form': form, 'lesson_plan': lesson_plan})


class LessonPlanDeleteView(View):
    def post(self, request, lessonplan_id):
        lesson_plan = get_object_or_404(LessonPlan, id=lessonplan_id)
        lesson_plan.delete()
        return redirect('lessonplan_list')


class LessonPlanDetailView(View):
    def get(self, request, lessonplan_id):
        lesson_plan = get_object_or_404(LessonPlan, id=lessonplan_id)
        return render(request, 'teacher/lessonplan_detail.html', {'lesson_plan': lesson_plan})


class LessonPlanListView(View):
    def get(self, request):
        lesson_plans = LessonPlan.objects.all()
        return render(request, 'teacher/lessonplan_list.html', {'lesson_plans': lesson_plans})
