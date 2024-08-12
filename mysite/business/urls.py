from django.urls import path

from . import views

app_name = "business"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:product_id>/enquire/", views.enquire, name="enquire"),
    path("<int:pk>/ordernow/", views.OrderView.as_view(), name="ordernow"),
]