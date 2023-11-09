from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True) # blank=True means that this field is optional
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that this field is automatically added
    datacompleted = models.DateTimeField(null=True, blank=True) # null=True means that this field is optional
    important = models.BooleanField(default=False)

    # on_delete=models.CASCADE means that if a user is deleted, all of their todos will be deleted as well
    user = models.ForeignKey(User, on_delete=models.CASCADE) 


    # title = models.CharField(max_length=100)
    # memo = models.TextField(blank=True) # blank=True means that this field is optional
    # created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that this field is automatically added
    # datecompleted = models.DateTimeField(null=True, blank=True) # null=True means that this field is optional
    # important = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE means that if a user is deleted, all of their todos will be deleted as well

    def __str__(self):
        return self.title

