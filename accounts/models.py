# User model for authentication

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # Creates a regular user
    def create_user(self, phone_no, password = None):
        # Checking for email and username
        if not phone_no:
            raise ValueError("Enter a valid phone number")

        # Adding the data to the model and registering
        user = self.model(
            phone_no = phone_no,
            password = password,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user



class User(AbstractBaseUser):
    """     Custom User model - Common to every user     """
    
    email_id = models.EmailField(
        primary_key = True,
        verbose_name = "Email ID",
        unique = True,
        null = False,
        blank = False,
        help_text = "Please enter applicants Email ID."
    )
    # PasswordField is provided by the AbstractBaseUser class
    # LastLoginField is provided by the AbstractBaseUser class
    date_joined = models.DateTimeField(
        verbose_name = 'Date joined',
        auto_now_add = True,
    )
    last_login = models.DateTimeField(
        verbose_name = 'Last login',
        auto_now = True,
    )
    is_official = models.BooleanField(
        verbose_name = 'official status',
        default = False,
    )
    is_applicant = models.BooleanField(
        verbose_name = 'applicant status',
        default = False,
    )
    USERNAME_FIELD = 'email_id'
    
    #objects = UserManager()
