from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """User manager class for custom user"""

    def create_user(self, email, password=None):
        """Creates and saves the user using email field"""
        if not email:
            raise ValueError("Users must have an email address!")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """Creates and saves the superuser"""
        user = self.create_user(email=email, password=password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def get_profile(self):
        return "http://localhost:8000" + self.profile.profile_picture.url


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, related_name='profile',
        on_delete=models.CASCADE, null=True, blank=True)
    bio = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profiles')

    def __str__(self):
        return str(self.user)
