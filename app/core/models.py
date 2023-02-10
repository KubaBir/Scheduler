from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        Permission, PermissionsMixin)
from django.db import models


# Create your models here.
class Test(models.Model):
    x = models.CharField(max_length=255)


class UserManager(BaseUserManager):
    def create_user(self, name, is_teacher=False, email=None, password=None):
        if not name:
            raise ValueError('Users must have a name')
        user = self.model(
            name=name,
            email=email,
            is_teacher=is_teacher
        )
        user.set_password(password)
        user.save(using=self._db)
        if is_teacher:
            permission = Permission.objects.get(name='Post a new lesson')
            user.user_permissions.add(permission)
        else:
            permission = Permission.objects.get(name='Join a lesson')
            user.user_permissions.add(permission)
        return user

    def create_superuser(self, name, password, is_teacher=False, email=None):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'


class Availability(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True}, related_name='teacher')
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': False}, related_name='student', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher.name} {self.date} {self.time}"

    class Meta:
        permissions = [
            ("add", "Post a new lesson"),
            ("join", "Join a lesson"),
        ]
