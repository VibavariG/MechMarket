from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Product
from .forms import EnquiryForm
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

class OrderView(generic.DetailView):
    template_name = "business/order.html"
    model = Product

def enquire(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            org = form.cleaned_data['org']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            success_message = f"Thank you, {firstname} {lastname}. We have received your message and will contact you at {email}."
            return render(request, 'business/enquire.html', {'form': EnquiryForm(), 'success_message': success_message, 'product':product})
        else:
            return render(request, 'business/enquire.html', {'form':form, 'product':product})
    else:
        form = EnquiryForm()
        return render(request, 'business/enquire.html', {'form': form, 'product':product})
