from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Follow
from .forms import PostForm


def index(request):
    form = PostForm()
    form.fields['body'].label = False
    posts = Post.objects.all().order_by('-post_time')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    return render(request, "network/index.html", {
        'form': form,
        'page_obj': page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def new_post(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)
    post = PostForm(request.POST)
    p = Post(poster= request.user, body= post.data['body'])
    p.save()
    return HttpResponseRedirect(reverse("index"))

def profile(request, user_id):
    '''
    Profile Page:
    1.the number of followers
    2.the number of people that the user follows
    3.all of the posts for that user, in reverse chronological order.
    '''
    user = User.objects.get(id = user_id)
    follows = Follow.objects.filter(follower= user).count()
    followers = Follow.objects.filter(user= user).count()
    user_posts = Post.objects.filter(poster= user).order_by('-post_time')
    follow_boolean = Follow.objects.filter(user= user, follower= request.user)

    paginator = Paginator(user_posts, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        "profile_user": user,
        "follows": follows,
        "followers": followers,
        'page_obj': page_obj,
        "follow_boolean": follow_boolean
    })

def follow(request, user_id, follower_id):
    user = User.objects.get(id = user_id)
    follower = User.objects.get(id = follower_id)
    f = Follow(user= user, follower= follower)
    f.save()
    return JsonResponse({"message": "Follow the user successfully."}, status=201)

def unfollow(request, user_id, follower_id):
    user = User.objects.get(id = user_id)
    follower = User.objects.get(id = follower_id)
    uf = Follow.objects.get(user= user, follower= follower)
    uf.delete()
    return JsonResponse({"message": "Unfollow the user successfully."}, status=201)

@login_required
def follow_posts(request):
    form = PostForm()
    form.fields['body'].label = False
    follow_users = [follow.user for follow in Follow.objects.filter(follower= request.user)]
    follow_posts = Post.objects.filter(poster__in= follow_users).order_by('-post_time')

    paginator = Paginator(follow_posts, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)

    return render(request, 'network/follow.html', {
        'form': form,
        'page_obj': page_obj,
    })

@login_required
def edit_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get("post_id", "")
        post_body = data.get("edit_body", "")
        post = Post.objects.get(id= post_id)
        if request.user == post.poster:
            post.body = post_body
            post.save()
        return JsonResponse({"message": "Post edit successfully."}, status=201)
    else:
        return JsonResponse({'error': "Invalid user or wrong method"}, status=404)
