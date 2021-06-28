from .models import User, Post, Comment,Category
from django.shortcuts import render, HttpResponse, redirect # add redirect to import statementcopy
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import bcrypt
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.db.models import Q 

#start page
def home(request):
    if 'userId' in request.session:
        return redirect('/home')
    return render(request,'log_reg.html')
#user functions
def registration(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            user_name = request.POST['user_name'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash)
        request.session['userId'] = user.id
        return redirect('/home')
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        user_list = User.objects.filter(email = request.POST['input'])
        if len(user_list) == 0:
            user = User.objects.get(user_name = request.POST['input'])
        else:
            user = User.objects.get(email = request.POST['input'])
        request.session['userId'] = user.id
        return redirect('/home')
def success(request,tag_slug=None):
    if 'userId' not in request.session:
        return redirect("/")
    all_posts = Post.objects.all()
    paginator =Paginator(all_posts,3)
    page = request.GET.get('page')
    all_posts = paginator.get_page(page)
    # search
    query = request.GET.get("q")
    if query:
        #all_posts = Post.objects.filter(title__icontains=query)
        all_posts=Post.objects.filter(Q(title__icontains=query)| Q(desc__icontains=query))
    context = {
        "user": User.objects.get(id=request.session['userId']),
        "all_posts": all_posts,
        "paginator":paginator,
        "categories":Category.objects.all(),
    }
    return render(request,'home.html',context)
#logout
def logOut(request):
    request.session.flush()
    return redirect("/")
#-------------------------------------------------------------------------
#posts functions
#show post 
def show_post(request,postId):
    this_post = Post.objects.get(id=postId)
    post_user = this_post.poster.id 
    all_post = Post.objects.all()
    #similar_posts = Post.objects.filter(Category=this_post.category).exclude(id=this_post.id)
    context = {
        "user": User.objects.get(id=request.session['userId']),
        "post": this_post,
        "similar_posts": Post.objects.filter(category=this_post.category).exclude(id=this_post.id),
        "users": this_post.liked.all(),
        "all_comment": Comment.objects.filter(post=postId),
    }
    return render(request, "show_post.html", context)
#show Category
def show_category(request,cats):
    cats = Category.objects.get(name = cats)
    cats_posts= Post.objects.filter(category=cats) 
    context = {
            "cats": cats,
            "cats_posts":cats_posts,
            "categories":Category.objects.all(),

    }
    return render(request, "show_category.html",context)
#add comment
def add_comment(request,postId):
    if request.method == 'POST':
        comment = Comment.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            body = request.POST['body'],
            post = Post.objects.get(id=postId)
        )
    return redirect (f'/show/{postId}')
#adding post
def add_post(request):
    if 'userId' in request.session:
        return render(request,'new.html')
    return render(request,'log_reg.html')
def new(request):
    if request.method == "POST" and request.FILES['image']:
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name , image)
        url = fs.url(filename)
        #check if there is an exiting category with the same name 
        cat_found = Category.objects.filter(name=request.POST['category'])
        if len(cat_found) == 0:
            categoryy = Category.objects.create(name=request.POST['category'])
        else:
            categoryy = cat_found[0]
        post = Post.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            body = request.POST['body'],
            category = categoryy,
            image = url,
            poster = User.objects.get(id = request.session['userId'])
        )
        user = User.objects.get(id = request.session['userId'])
        user.posts.add(post)
        request.session['userId'] = user.id
        return redirect('/home')   
#editing a post
def edit_post(request,postId):
    if 'userId' in request.session:
        context ={
            "post" : Post.objects.get(id = postId)
        }
        return render(request,'edit.html',context)
    return render(request,'log_reg.html')
def make_edit(request,postId):
    if request.method == "POST":
        errors = Post.objects.post_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/edit/{postId}")
        post = Post.objects.get(id = postId)
        post.title = request.POST['title']
        post.desc = request.POST['desc']
        post.body = request.POST['body']
        #check if there is an exiting category with the same name 
        cat_found = Category.objects.filter(name=request.POST['category'])
        if len(cat_found) == 0:
            categoryy = Category.objects.create(name=request.POST['category'])
        else:
            categoryy = cat_found[0]
        post.category= categoryy
        #image uplouding
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name , image)
        url = fs.url(filename)
        post.image = url
        post.save()
    return redirect("/")
#deleting a post
def delete_post(request,postId):
    post = Post.objects.get(id = postId)
    post.delete()
    return redirect("/")
#liking a post
def like(request,postId):
    user = User.objects.get(id = request.session['userId'])
    user.liked_posts.add(Post.objects.get(id = postId))
    return redirect("/")
#unliking a post    
def unlike(request,postId):
    user = User.objects.get(id = request.session['userId'])
    user.liked_posts.remove(Post.objects.get(id = postId))
    return redirect("/")
#------------------------------------------------------------------------------------
#user profile
def profile(request):
    if 'userId' in request.session:
        context = {
            'user' : User.objects.get(id = request.session['userId'])
        }
        return render(request,'profile.html',context)
    return render(request,'log_reg.html')
#------------------------------------------------------------------------------------
#search
def search(request):
    query = request.GET['query']
    all_posts = Post.objects.filter(title__icontains=query)
    context = {
        'all_posts':all_posts
    }
    return render(request,'search.html',context)

#-------------------------------------------------------------------------    
#contact
def contact(request):

    return render(request,'contact.html')

#-------------------------------------------------------------------------    
#about
def about(request):
    return render(request,'about.html')
