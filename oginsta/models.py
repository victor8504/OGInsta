from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile_pic/', null = True)
    bio = models.TextField(max_length = 50, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 25, blank = True)
    caption = models.TextField(blank = True)
    likes = models.PositiveIntegerField(default = 0)
    date_posted = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class Comment(models.Model):
    comment = models.CharField(max_length = 150, blank = True)
    date_commented = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image)

    def save_comment(self):
        self.save()
    
    def __str__(self):
        return self.comment
