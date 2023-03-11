from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField()
    likes = models.IntegerField(default=0)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    status = models.CharField(max_length=2,
    choices=Status.choices,
    default=Status.DRAFT)

class Talaba(models.Model):
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    guruh_raqami = models.IntegerField()
    fakultet_nomi = models.CharField(max_length=255)
    ortacha_baho = models.IntegerField()
    def __str__(self):
        return self.name
    
class Meta:
    ordering = ['-publish']    
    indexes = [
        models.Index(fields=['-publish']),
        ]    



        