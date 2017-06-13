import datetime

from django.db import models
from django.utils import timezone()


# Create your models here.
class Blogpost(models.Model):
    blog_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.blog_title

    
class Comment(models.Model):
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.content