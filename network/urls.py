
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_post, name="new"),
    path("follow_posts", views.follow_posts, name="follow_posts"),
    path("edit_post", views.edit_post, name="edit_post"),
    path("like_post", views.like_post, name="like_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow/<int:user_id>/<int:follower_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>/<int:follower_id>", views.unfollow, name="unfollow")

]
