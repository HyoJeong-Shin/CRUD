from django.contrib import admin

# Register your models here.
from .models import Post    #import class Post from models.py

admin.site.register(Post)   #register class Post --> Blog.Post shows up in 'admin/' page