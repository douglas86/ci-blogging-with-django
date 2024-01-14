from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

"""
The @admin.register(Post)
This is how we register a class for the admin site
This will allow us to customize the admin site behaviour
"""


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')  # shows title, slug, status and created_on of each post
    search_fields = ['title']  # can now search the post based on title
    list_filter = ('status',)  # creates a filter by status on the right side of an admin panel
    prepopulated_fields = {'slug': ('title',)}  # this will autopopulate slug filed by the title
    summernote_fields = ('content',)  # adds the rich text editor from summernote app to the content section


# Register your models here.
admin.site.register(Comment)
