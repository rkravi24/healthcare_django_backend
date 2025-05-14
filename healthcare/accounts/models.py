from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    
    # Make the username field optional as we'll use email for login
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=255)
    
#     # Make the username field optional as we'll use email for login
#     username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    
#     # Override these fields to fix the naming conflicts
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         related_name='accounts_user_set',  # Custom related_name
#         related_query_name='accounts_user',
#     )
    
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         related_name='accounts_user_set',  # Custom related_name
#         related_query_name='accounts_user',
#     )
    
#     objects = UserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
    
#     def __str__(self):
#         return self.email
