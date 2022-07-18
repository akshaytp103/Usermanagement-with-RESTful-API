from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name,  username, email, password=None):
         if not email:
            raise ValueError('Users must have an email address')

         if not username:
            raise ValueError('Users must have a username address')
            
         user = self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name
         )

         user.set_password(password)
         user.save(using=self._db)
         return user




class Account(AbstractBaseUser):
    
    name             = models.CharField(max_length=50)
    username         = None
    email            = models.EmailField(max_length=100, unique=True)
    phone_number     = models.CharField(max_length=50)
    password         = models.CharField(max_length=255)
    dob              = models.DateField()
    profile_picture  = models.ImageField(upload_to='photos/profile')

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
