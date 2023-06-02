from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class ChiefExecutive(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def grant_manage_everything_permission(self):
        content_type = ContentType.objects.get_for_model(self)
        permission = Permission.objects.create(
            codename='can_manage_everything',
            name='Can Manage Everything',
            content_type=content_type,
        )
        self.user_permissions.add(permission)

class HeadTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)
    teachers = models.ManyToManyField('teacher.Teacher')

    class Meta:
        permissions = [
            ('view_teacher', 'Can view teacher details'),
            ('add_teacher', 'Can add new teacher'),
            ('change_teacher', 'Can update teacher details'),
            ('delete_teacher', 'Can delete teacher'),
        ]

    def __str__(self):
        return self.name

class Secretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ('view_payment_history', 'Can view payment history'),
            ('add_payment', 'Can add new payment'),
            ('change_payment', 'Can update payment details'),
        ]

    def __str__(self):
        return self.name
