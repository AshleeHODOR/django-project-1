#view class in django - template - renders templates
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
