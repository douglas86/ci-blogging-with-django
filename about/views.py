from django.views.generic import ListView

from about.models import About


# Create your views here.
class AboutList(ListView):
    template_name = 'about/about.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Fetches about data from the database model
        :return: all objects from a database in reverse order by updated_on
        """
        return About.objects.all().order_by('-updated_on').first()

    def get_context_data(self, **kwargs):
        return {'about': self.get_queryset()}
