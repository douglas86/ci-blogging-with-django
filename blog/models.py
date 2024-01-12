from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        What is a Meta Class?
        Metadata is data about data

        In this situation the ordering means order the data based on a field
        In this case created_on field
        The '-' in front of created on means in reverse direction
        """
        ordering = ['-created_on']  # ordering is used to order the field in question

    def __str__(self):
        """
        What is the __str__ method?
        This method is used to return a description of the class
        In this situation it will return the title of the class
        As I have connected it to the admin panel instead of it showing the Object
        It will show the string
        :return:
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
