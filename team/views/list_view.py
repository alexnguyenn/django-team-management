from django.views.generic import TemplateView

from team.models import Member


class MemberListView(TemplateView):
    template_name = "team/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = Member.objects.all()
        context["member_count"] = Member.objects.count()
        return context
