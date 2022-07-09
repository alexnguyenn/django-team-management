from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from team.models import Member


class MemberCreateView(CreateView):
    model = Member
    fields = ["first_name", "last_name", "email", "phone", "role"]
    success_url = reverse_lazy("team:list")
    template_name = "team/form.html"


class MemberUpdateView(UpdateView):
    model = Member
    fields = ["first_name", "last_name", "email", "phone", "role"]
    success_url = reverse_lazy("team:list")
    template_name = "team/form.html"


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy("team:list")
    template_name = "team/delete.html"
