from django.contrib import admin
from . models import Job_Model, Application
# Register your models here.

@admin.register(Job_Model)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'location', 'recruiter', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'recruiter']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['recruiter']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
    
    
@admin.register(Application) 
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'post', 'created', 'active']
    list_filter = ['created', 'active']
    search_fields = ['name', 'email', 'phone']
    

