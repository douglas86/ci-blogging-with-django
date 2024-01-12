from django.shortcuts import render
from django.views import generic
from .models import Post

"""
generic.ListView - 
    The advantage of using this type of view is that you don't have to add the HTML  template only the model
"""


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'
