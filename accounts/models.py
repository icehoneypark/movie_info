from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
        followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')