from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SuperUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SuperUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = SuperUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    total_count = models.IntegerField()

    def __str__(self):
        return self.title


class Borrow(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('returned', 'Returned'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"
