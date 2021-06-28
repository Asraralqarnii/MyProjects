from django.db import models
import re
import bcrypt
from datetime import datetime, timedelta

class UserManager(models.Manager):
    def register_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Fisrt name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData["password"] != postData["con_pw"]:
            errors["con_pw"] = "Passwords should be match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        user_list = User.objects.filter(email=postData['email'])
        if len(user_list) > 0:
            errors['not_unique'] = "Email is already exists"
        if len(postData['user_name']) < 2:
            errors["user_name"] = "User name should be at least 2 characters"
        user_list = User.objects.filter(email=postData['user_name'])
        if len(user_list) > 0:
            errors['not_unique'] = "User Name is already exists"
        return errors
    
    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['input']):
            user_list = User.objects.filter(user_name=post_data['input'])
            if len(user_list) == 0:
                errors['user_name'] = "User Name is not found"
            #elif len(user_list) == 1:
                #user_list = User.objects.filter(user_name=post_data['input'])
        else:
            user_list = User.objects.filter(email=post_data['input'])
        if len(user_list) == 0:
            errors['user_name'] = "Email or user name is not found"
        else: 
            if len(post_data['password']) < 8:
                errors['password'] = "Password must be at least 8 characters, please"
            elif not bcrypt.checkpw(post_data['password'].encode(), user_list[0].password.encode()):
                errors['match'] = "Password is not correct"
        return errors
class User(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
#-----------------------------------------------------------------
class PostManager(models.Manager):
    def post_validator(self,postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "A post must be consist of at least 3 characters"
        if len(postData['desc']) < 3:
            errors["desc"] = "A description must be provided!"
        return errors

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    body = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True,on_delete = models.CASCADE,related_name ="cat")
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/') #this
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    poster = models.ForeignKey(User, related_name="posts" , on_delete = models.CASCADE)
    liked = models.ManyToManyField(User,related_name ="liked_posts")
    objects = PostManager()

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=45, unique=True)
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)