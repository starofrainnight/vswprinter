from django.views.generic import TemplateView
from . import get_template_name


class IndexView(TemplateView):
    template_name = get_template_name("index.html")
