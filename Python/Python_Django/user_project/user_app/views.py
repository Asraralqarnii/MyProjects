from django.shortcuts import render, redirect
from user_app.models import User

def index(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request,"index.html",context)

def add(request):

    firstname_form = request.POST['first_name']
    lastname_form = request.POST['last_name']
    email_from_form = request.POST['email']
    age_from_form = request.POST['age']

    User.objects.create(
        first_name = firstname_form,
        last_name = lastname_form,
        email = email_from_form,
        age = age_from_form,
        )

    return redirect("/")
