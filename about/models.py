from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Order content based on updated_on field in reverse order
        """
        ordering = ('-updated_on',)

    def __str__(self):
        """
        Display the title of the about models
        :return:
        """
        return self.title
