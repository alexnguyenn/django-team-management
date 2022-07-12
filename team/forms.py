from django import forms

from team.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "email", "phone", "role"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes and placeholders
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control" if field != "role" else "form-select",
                    "placeholder": self.fields[field].label,
                }
            )
