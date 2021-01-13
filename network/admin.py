from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "poster", "body", "post_time")


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
