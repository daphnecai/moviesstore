from django.urls import path
from . import views

app_name = "petitions"

urlpatterns = [
    path("", views.petition_list, name="list"),
    path("new/", views.petition_create, name="create"),
    path("<int:petition_id>/vote/", views.petition_vote, name="vote"),
]
