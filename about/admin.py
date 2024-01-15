from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content', 'updated_on')  # display title, content and updated_on for each about section
    search_fields = ['title']  # search by title
    summernote_fields = ('content',)  # use summernote to add rich text to content
