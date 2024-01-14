from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

"""
generic views - 
    Generic views are beneficial for dealing with repetitive full-stck coding tasks such as displaying database contents
    to a webpage. It handles teh most common use cases in web app development.
generic.ListView - 
    The advantage of using this type of view is that you don't have to add the HTML  template only the model
    
Three types of views that Django offers:
- Generic:
    - Requires little customisation
    - Works out of the box
    - Limited ability to extend
- Class Based:
    - Similar syntax to generic views
    - Views can be reused
    - Conceptually difficult to grasp
- Function Based:
    - Simpler and easier to understand
    - More explicit
    - Very flexible
"""


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
     An instance of :model:`blog.Post`.

     **Template**
     :template:`blog/post_detail.html`

    :param request:
    :param slug:
    :return:
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    context = {'post': post, 'coder': 'Douglas Maxton'}

    return render(
        request, "blog/post_detail.html", context
    )
