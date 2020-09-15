from django.db import models

# Create your models here.
class BlogPost(models.Model):
    blogTitle= models.CharField(max_length=300)
    blogContent = models.TextField()
    blogDatePost = models.DateTimeField()

    def __str__(self):
        return self.blogTitle
class SkillsAndTechnology(models.Model):
    nameSkill = models.CharField(max_length=500)
    contentSkills = models.TextField()
    testing = models.TextField()
    



    

