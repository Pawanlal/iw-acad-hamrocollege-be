import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


def file_location(instance, filename):
    extension = filename.split('.')[-1]
    user_id = str(instance.id)
    unique_id = str(uuid.uuid4())
    new_filename = unique_id+'.'+extension

    file_path = 'profile/{user_id}/{new_filename}'.format(
        user_id=user_id,
        new_filename=new_filename
    )
    return file_path


def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = (instance.first_name + "." + instance.last_name).lower()
        counter = 1
        while User.objects.filter(username=username):
            username = username + str(counter)
            counter += 1
        instance.username = username


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must have first name")
        if not last_name:
            raise ValueError("User must have last name")
        # if not username:
        #     raise ValueError("User must have an username")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
            # username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
            # username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # constants in model class
    ADMIN = 0
    TEACHER = 1
    LIBRARIAN = 2
    STUDENT = 3
    USER_ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (LIBRARIAN, 'Librarian'),
        (STUDENT, 'Student'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=150, unique=True)
    profile = models.ImageField(upload_to=file_location, null=True, blank=True)
    user_role = models.IntegerField(choices=USER_ROLE_CHOICES, default=STUDENT,)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', ]
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


models.signals.pre_save.connect(set_username, sender=User)
