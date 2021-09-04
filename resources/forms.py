from django import forms
from martor.fields import MartorFormField


class PostCreateForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "aria-label": "postname",
                "aria-describedby": "basic-addon1",
                "placeholder": "Post title is required",
            }
        ),
    )
    content = MartorFormField()
    is_private = forms.BooleanField(required=False)


class FileCreateForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "aria-label": "filename",
                "aria-describedby": "basic-addon1",
                "placeholder": "Filename is optional",
            }
        ),
    )
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "type": "file",
                "class": "custom-file-input",
                "id": "inputGroupFile01",
                "aria-describedby": "inputGroupFileAddon01",
            }
        )
    )
    is_private = forms.BooleanField(required=False)
