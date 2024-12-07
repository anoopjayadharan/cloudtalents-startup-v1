from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, ImageUploadForm
from .models import Image


# Home Page View
def home(request):
    if request.user.is_authenticated:
        return redirect('image_list')
    return render(request, 'home.html')


# User Logout View
def user_logout(request):
    logout(request)
    return redirect('home')


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('upload_image')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# User Login View

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return '/images/'


# Image Upload View
@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('image_list')

    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


# List of User Images
@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'images': images})
