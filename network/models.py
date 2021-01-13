from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class Post(models.Model):
    body = RichTextField(blank= True, null= True)
    poster = models.ForeignKey(User, on_delete= models.CASCADE, related_name='poster')
    post_time = models.DateTimeField(auto_now_add= True)
    likes = models.ManyToManyField(User, related_name='like_users')

    def __str__(self):
        return(f"{self.poster} at {self.post_time} said {self.body}")

    def serialize(self):
        return {
            "body": self.body,
            "poster": self.poster.username,
            "post_time": self.post_time.strftime("%b %-d %Y, %-I:%M %p"),
            "likes": [user.username for user in self.likes.all()]
        }