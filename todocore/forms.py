from django import forms

from todocore.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    deadline = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={"type": "date", "input_formats": ["%Y-%m-%d"]},
            time_attrs={"type": "time", "input_formats": ["%H:%M"]},
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"
