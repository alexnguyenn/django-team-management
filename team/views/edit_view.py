from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from team.forms import MemberForm
from team.models import Member


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy("team:list")
    template_name = "team/form.html"


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy("team:list")
    template_name = "team/form.html"


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy("team:list")
    template_name = "team/delete.html"
