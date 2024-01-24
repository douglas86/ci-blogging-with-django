from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib import messages

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
    comments = post.comments.all().order_by('-created_on')
    comments_count = post.comments.filter(approved=True).count()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_count': comments_count,
               'comment_form': comment_form}

    return render(
        request, "blog/post_detail.html", context
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == 'POST':
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating commit!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete a comment
    :param request:
    :param slug:
    :param comment_id:
    :return:
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
