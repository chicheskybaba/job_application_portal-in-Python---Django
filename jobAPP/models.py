from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Job_Model.Status.PUBLISHED)




class Job_Model(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_posts')
    body = models.TextField()
    location = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    
    objects = models.Manager()       # The default manager.
    published = PublishedManager()   # Our Custom Manager.
    
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        
    def __str__(self):
        return self.title
        
        
        
        
        
        # Comment = Application
        # Post = Job_Model
        # body = coverletter
        


class Application(models.Model):
    post = models.ForeignKey(Job_Model, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    coverletter = models.TextField(max_length=1500)
    cv = models.FileField(blank=True, null=True, upload_to='cvs')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        
        
    def __str__(self):
        return f'Application from {self.name} for the Position of {self.post}'
        
        
