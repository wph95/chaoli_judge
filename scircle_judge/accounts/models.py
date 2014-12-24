# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    level = models.IntegerField('难度等级', default=0)
