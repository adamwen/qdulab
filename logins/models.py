from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    real_name = models.CharField(max_length=8, null=False, blank=False)
    school_id = models.CharField(max_length=12, null=False, blank=False)
    phone_num = models.CharField(max_length=11, null=False, blank=False)
