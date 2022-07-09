from django.urls import path

from team.views import (
    MemberCreateView,
    MemberDeleteView,
    MemberListView,
    MemberUpdateView,
)

app_name = "team"

urlpatterns = [
    path("", MemberListView.as_view(), name="list"),
    path("new/", MemberCreateView.as_view(), name="new"),
    path("edit/<int:pk>/", MemberUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", MemberDeleteView.as_view(), name="delete"),
]
