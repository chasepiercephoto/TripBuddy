from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create (
                first_name= request.POST['first_name'],
                last_name= request.POST['last_name'],
                email= request.POST['email'],
                password= pw_hash,
            )
            user = User.objects.last()
            request.session['userid'] = user.id
            return redirect('/dashboard')
def login(request):
    if request.method == "POST":
        errors = User.objects.log_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['userid'] = user.id
            return redirect('/dashboard')

def dashboard(request):
    if 'userid' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'trip': Trip.objects.all(),
    }

    return render(request, 'dashboard.html', context)

def new_trip_form(request):
    
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'trip': Trip.objects.all(),
    }

    return render(request, 'new_trip.html', context)

def new_trip(request):
    Trip.objects.create(
    destination = request.POST["destination"],
    start_date = request.POST["start_date"],
    end_date = request.POST["end_date"],
    plan = request.POST["plan"],
    createdBy= User.objects.get(id=request.session['userid']))
    return redirect('/dashboard')