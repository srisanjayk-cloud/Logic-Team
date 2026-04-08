from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event , Project


def home(request):
    events = Event.objects.filter(date__gte=datetime.now()).order_by('date')
    projects = Project.objects.all().order_by('-id')  # or any order you like
    
    context = {
        'events': events,
        'projects': projects,
        'year': datetime.now().year
    }

    return render(request, 'home.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def register(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password != confirm:
            error = "Passwords do not match"
        elif User.objects.filter(username=username).exists():
            error = "Username already taken"
        else:
            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return redirect('/')

    return render(request, 'signup.html', {'error': error})



def user_logout(request):
    auth_logout(request)
    return redirect('/')


def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events.html', {'events': events})

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})



@login_required
def event_create(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            location=request.POST.get('location'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            tags=request.POST.get('tags'),
            created_by=request.user   
        )
        return redirect('events')
        
    return render(request , 'create_event.html')




@login_required
def project_create(request):
    if request.method == 'POST':
        Project.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            tech_stack = request.POST.get('tech_stack'),
            github_link = request.POST.get('github_link'),
            demo_link = request.POST.get('demo_link'),
            created_at = timezone.now(),
            created_by=request.user

  
        )
        return redirect('projects')
        
    return render(request , 'create_project.html')

