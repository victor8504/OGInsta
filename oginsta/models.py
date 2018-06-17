from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile_pic/', null = True)
    bio = models.TextField(max_length = 50, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 25, blank = True)
    caption = models.TextField(blank = True)
    likes = models.PositiveIntegerField(default = 0)
    date_posted = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)



