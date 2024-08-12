from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Product
from django.utils import timezone


# Create your views here.

class IndexView(generic.ListView):
    template_name = "business/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(choice__isnull=False).distinct().filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]