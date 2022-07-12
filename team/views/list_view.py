from django.views.generic import ListView

from team.models import Member


class MemberListView(ListView):
    template_name = "team/list.html"
    model = Member
    context_object_name = "members"
