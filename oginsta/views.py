from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, Comment, Like

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get(username = username)
    images = Image.objects.filter(user_id = user)
    profile = Profile.objects.get(user=user)

    return render(request, 'profile.html', {"user": user,"images": images,"profile": profile})