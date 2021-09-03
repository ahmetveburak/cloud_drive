from django import forms
from tempus_dominus.widgets import DateTimePicker


class TokenCreateForm(forms.Form):
    enabled_count = forms.IntegerField(required=False, min_value=0, initial=0)
    enabled_to = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(
            options={"useCurrent": True, "collapse": False},
            attrs={"append": "fa fa-calendar", "icon_toggle": True, "size": "small"},
        ),
    )


class TokenAdminFrom(forms.ModelForm):
    token = forms.CharField(
        label="Dosya Adı",
        widget=forms.TextInput(attrs={"size": 35, "readonly": True}),
        help_text="This token generated automatically.",
    )
