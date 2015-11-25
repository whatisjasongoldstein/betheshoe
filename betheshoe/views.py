from django.views.generic import TemplateView
from movies.models import Movie

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['promoted_movie'] = Movie.objects.filter(publish=True, image__gt="").order_by('-year').first()
        return context

class Privacy(TemplateView):
    template_name = "privacy.html"