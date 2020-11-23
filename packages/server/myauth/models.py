from django.db import models
from django.contrib.auth.models import AbstractBaseUser

"""
User Model:
  email = Email field, required
  username = Char field required
  name = Char field required
  is_mobile_verified = Boolean field, default: false
  is_email_verified = Boolean field, default: false
"""

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(max_length=254)
  username = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  is_mobile_verified = models.BooleanField(default=False)
  is_email_verified = models.BooleanField(default=False)

  USERNAME_FIELD = "username"
