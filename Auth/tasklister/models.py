from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(max_length=255, unique=True,)
    is_active = models.BooleanField(default=True,)
    is_admin = models.BooleanField(default=False,)
    is_staff = models.BooleanField(default=False,)
    is_superuser = models.BooleanField(default=False,)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True,)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True,)
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
class Task(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.CharField(max_length=255)
    completed = models.BooleanField(default = True)
    Created_at = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=25)
    User = models.ForeignKey(User, on_delete=models.CASCADE)






