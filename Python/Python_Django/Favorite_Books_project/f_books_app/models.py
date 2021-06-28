from django.db import models
import re
import bcrypt
from datetime import datetime, timedelta
# Create your models here.


class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # check first name  at least 2 characters
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters!"
        # check last name at least 2 characters
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters!"
        Email = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not Email.match(post_data['email']):
            errors['email'] = "Please, enter valid email"
        # check password char len 8
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters, please"
        # check confirm password == password
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Confirm password does not match Password, try again!"
        print("reached the validator for register")

        # unique email
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) > 0:
            errors['not_unique'] = "Email is already exists"
        return errors


    def login_validator(self, post_data):
        errors = {}
        Email = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not Email.match(post_data['email']):
            errors['email'] = "Invalid email format!"
        # check password char len 8
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        # check if email is in db
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) == 0:
            errors['email2'] = "Email was not found , Enter registered email"
        elif not bcrypt.checkpw(post_data['password'].encode(), user_list[0].password.encode()):
            errors['match'] = "Password does not correct,try again!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=100)
    # books
    # liked_books
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class BookManager(models.Manager):
    def books_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 3:
            errors['title'] = "title must be at least 3 characters"
        if len(post_data['desc']) < 5:
            errors['desc'] = "Description must be at least 5 characters"
        
        return errors


class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    upload_by = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
    fav_by = models.ManyToManyField(User, related_name="fav_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()