from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        errors = {}

        if len(post_data['first_name']) < 3:
            errors['first_name'] = "please enter a name of at least 3 characters"
        if len(post_data['last_name']) < 3:
            errors['last_name'] = "please enter a real last name"
        # elif int(post_data['year']) < 1880:
        #     errors['year'] = "please enter a year after 1880"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid Email address"
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors['email'] = "Email already taken"
        if len(post_data['password']) < 8:
            errors['reg_pw'] = "Your password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_pw'] = "Passwords do not match"


        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    confirmPW = models.CharField(max_length=100)

    # objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trip(models.Model):
    destination = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    creator = models.ForeignKey(User, related_name="createdBy", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)