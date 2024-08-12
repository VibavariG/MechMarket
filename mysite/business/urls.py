from django.urls import path

from . import views

app_name = "business"
urlpatterns = [
    # ex: /business/
    path("", views.index, name="index")
    # path("", views.IndexView.as_view(), name="index"),
    # ex: /business/5/
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # # ex: /business/5/results/
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]