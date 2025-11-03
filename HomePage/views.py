from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "HomePage/index.html"


class AboutView(TemplateView):
    template_name = "HomePage/about.html"


class ProductView(TemplateView):
    template_name = "HomePage/product.html"


class PricingView(TemplateView):
    template_name = "HomePage/pricing.html"


class CustLoginView(TemplateView):
    template_name = "common/login.html"
