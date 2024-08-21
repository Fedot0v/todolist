from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_complete",
            "tags",
        ]
        widgets = {
            "deadline": forms.DateInput(format="%m/%d/%Y", attrs={"type": "date"}),
            "tags": forms.CheckboxSelectMultiple(),
        }