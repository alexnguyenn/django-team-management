from django.urls import path

from team.views import ListView

urlpatterns = [
    path("", ListView.as_view(), name="list_view"),
]
