from django.contrib import admin
from .models import Post, CommunityComment 
# Register your models here.

admin.site.register(Post)
admin.site.register(CommunityComment)