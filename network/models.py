from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class Post(models.Model):
    body = RichTextField(blank= True, null= True)
    poster = models.ForeignKey(User, on_delete= models.CASCADE, related_name='poster')
    post_time = models.DateTimeField(auto_now_add= True)
    like = models.ManyToManyField(User, blank= True)
    def __str__(self):
        return(f"{self.poster} at {self.post_time} said {self.body}")

    def serialize(self):
        return {
            "body": self.body,
            "poster_id": self.poster.id,
            "poster": self.poster.username,
            "post_time": self.post_time.strftime("%b %-d %Y, %-I:%M %p")
        }

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name='follower')
    follow_time = models.DateField(auto_now_add= True)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete= models.CASCADE)
#     liker = models.ForeignKey(User, on_delete= models.CASCADE)
#     like_time = models.DateTimeField(auto_now_add= True)