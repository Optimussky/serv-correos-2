from django.db import models
#import uuid

class Notification(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uuid = models.CharField(max_length=250)
    body = models.TextField()
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)


