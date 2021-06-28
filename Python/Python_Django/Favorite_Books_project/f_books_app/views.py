from django.shortcuts import render, redirect
from .models import User , Books
from django.contrib import messages
import bcrypt
from datetime import date
# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect("/books")
    context = {
        'today': date.today()
    }
    return render(request,"reg_log.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")

        password = request.POST['password']
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash
        print(password_hash)

        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=password_hash)
        request.session['user_id'] = new_user.id
        return redirect("/books") 


def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
            
        logged_user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = logged_user.id
        return redirect('/books')
    return redirect("/")

def fav_books(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_books": Books.objects.all(),
    }
    return render(request,"fav_books.html", context)

def fav_book(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Books.objects.get(id=id)
    book.fav_by.add(user)
    return redirect("/books")

def add_book(request):
    if request.method == "POST":
        errors = Books.objects.books_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("errors have been found")
            return redirect("/books")
        
        Books.objects.create(
            title=request.POST['title'],
            description=request.POST['desc'],
            upload_by=User.objects.get(id=request.session['user_id'])
        )
        print("new recipe has been created")
    return redirect("/books")

def fav_book_info(request,id):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "session_user": User.objects.get(id=request.session['user_id']),
        "all_books": Books.objects.all(),
        "all_users": User.objects.all(),
        "book":Books.objects.get(id=id)
    }
    return render(request,"book_info.html",context)

def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
    return redirect("/")
    
def unfav_book(request,id):
    user = User.objects.get(id=request.session['user_id'])
    book = Books.objects.get(id=id)
    book.fav_by.remove(user)
    return redirect("/books")

def delete_book(request):
    book = Books.objects.get(id=r_id)
    book.delete()
    return redirect("/books")

def update(request,id):
    if request.method == "POST":
        errors = Books.objects.books_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("errors have been found")
            return redirect(f"/books/{id}")
        under_30 = False
        if request.POST['under_30'] == "true":
            under_30 = True
        book = Books.objects.get(id=r_id)
        book.title = request.POST['title']
        recipe.description = request.POST['desc']
        recipe.save()
        return redirect(f"/books/{id}")