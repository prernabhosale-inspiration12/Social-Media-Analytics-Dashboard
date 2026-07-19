from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            "department_name",
            "department_code",
            "description",
        ]

        widgets = {
            "department_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Department Name"
            }),

            "department_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Department Code"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Description"
            }),
        }

    def clean_department_name(self):

        department_name = self.cleaned_data["department_name"]

        qs = Department.objects.filter(
            department_name__iexact=department_name
        )

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Department already exists."
            )

        return department_name