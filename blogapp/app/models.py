from django.db import models

# Create your models here.
class BlogPost(models.Model):
    blogTitle= models.CharField()
    blogContent = models.TextField()
    blogDatePost = models.DateTimeField()

    
    

