from django.urls import path

from . import views

app_name = "business"
urlpatterns = [
    # ex: /business/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /business/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # # ex: /business/5/results/
    path("<int:product_id>/enquire/", views.enquire, name="enquire"),
    # # ex: /polls/5/vote/
    path("<int:product_id>/ordernow/", views.ordernow, name="ordernow"),
]