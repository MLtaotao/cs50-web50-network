from django.test import Client, TestCase
import unittest
from datetime import datetime

from .models import User, Post

# Create your tests here.
class NetworkTestCase(TestCase):

    #creat user 1 and user 2
    def set_up(self):
        u1 = User.objects.create(
            username= 'abc', email='abc@example.com', password='abc'
        )
        u1 = User.objects.create(
            username= 'def', email='def@example.com', password='def'
        )

    #test index
    def test_index(self):
        # Set up client to make requests
        c = Client()

        # Send get request to index page and store response
        response = c.get("")

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        respeonse = c.get("/login")
        self.assertEqual(response.status_code, 200)

    #creat new post
    def new_post(self):
        p1 = Post.objects.create(
            poster = User.objects.get(username='abc'),
            body = 'abcdef'
        )

 