from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order content based on title in ascending order
        """
        ordering = ('title',)

    def __str__(self):
        """
        Display the title of the about models
        :return:
        """
        return self.title
