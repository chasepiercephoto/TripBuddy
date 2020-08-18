from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 3:
            errors['title'] = "please enter a title of at least 3 characters"
        if len(post_data['year']) < 1:
            errors['year'] = "please enter a year"
        elif int(post_data['year']) < 1880:
            errors['year'] = "please enter a year after 1880"
        if len(post_data['director']) < 3:
            errors['director'] = "please enter a longer name"
        if len(post_data['studio']) < 3:
            errors['studio'] = "please enter a real studio"


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