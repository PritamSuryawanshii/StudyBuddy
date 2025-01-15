from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   # description can be blank  & forms cant be blank
    # participants = models.ManyToManyField(
    # User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)       # save value updated every single time (auto_now)
    created = models.DateTimeField(auto_now_add=True)   # only take timstamp if we save multiple times value never change (auto_now_add)

    class Meta:
        ordering = ['-updated', '-created']
        # display the new updated value first

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[0:50]