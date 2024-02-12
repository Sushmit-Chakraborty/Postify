from django.db import models

# Create your models here.
class Posts(models.Model):
    postTitle = models.CharField(max_length=100)
    postContent = models.TextField()