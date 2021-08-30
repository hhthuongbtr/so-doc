# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    team_in_department = models.CharField(max_length=6)
    # More info from CAS
    department = models.CharField(max_length=6)
    division_code = models.CharField(max_length=6)
    team_code = models.CharField(max_length=6)
    mobile_phone = models.CharField(max_length=15)

class CustomuserUserWhiteList(models.Model):
    customuser = models.ForeignKey(CustomUser, models.DO_NOTHING)
    reason = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'accounts_customuser_user_white_list'
