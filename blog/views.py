from django.shortcuts import render
from django.views import generic
from .models import Post

"""
generic views - 
    Generic views are beneficial for dealing with repetitive full-stck coding tasks such as displaying database contents
    to a webpage. It handles teh most common use cases in web app development.
generic.ListView - 
    The advantage of using this type of view is that you don't have to add the HTML  template only the model
"""


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
