from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, Comment, Like
from .forms import PostForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user_id = user)
    profile = Profile.objects.get(user=request.user)

    return render(request, 'profile.html', {"current_user": current_user,"images": images,"profile": profile})


@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.name = current_user
                    post.profile = profile
                    post.save()
                    return redirect('home')
            else:
                form = PostForm()

    return render(request, 'post.html', {"post_form": form,"user": current_user})