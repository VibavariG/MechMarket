from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Product
from django.utils import timezone


# Create your views here.

# def index(request):
#     return HttpResponse("Hi, it's the index page")
class IndexView(generic.ListView):
    template_name = "business/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        """Return available products"""
        return Product.objects.filter(date_released__lte=timezone.now())
        #todo - order by popularity?

class DetailView(generic.DetailView):
    template_name = "business/detail.html"
    model = Product

def enquire(request, product_id):
    return HttpResponse("Enquiring about product %s." % product_id)

def ordernow(request, product_id):
    return HttpResponse("Ordering product %s." % product_id)