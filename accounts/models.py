# User model for authentication

from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    # Creates a regular user
    def create_user(self, email, password, **extra_fields):
        # Checking for email
        if not email:
            raise ValueError("Enter a valid Email ID")
        email = self.normalize_email(email)
        # Adding the data to the database and registering
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    # Creates a super user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    """     Custom User model - Common to every user     """
    username = None
    first_name = None
    last_name = None
    ''''full_name = models.CharField(
        max_length = 50,
        verbose_name = 'Full Name',
        blank = False,
        null = False,
    )'''
    email = models.EmailField(
        primary_key = True,
        verbose_name = "Email ID",
        unique = True,
        null = False,
        blank = False,
        help_text = "Please enter applicants Email ID."
    )
    # PasswordField is provided by the AbstractBaseUser class
    # LastLoginField is provided by the AbstractBaseUser class
    is_official = models.BooleanField(
        verbose_name = 'official status',
        default = False,
    )    # PasswordField is provided by the AbstractBaseUser class
    # LastLoginField is provided by the AbstractBaseUser class
    is_applicant = models.BooleanField(
        verbose_name = 'applicant status',
        default = True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        #full_name
    ]
    objects = UserManager()
    
    def __str__(self):
        return self.full_name
