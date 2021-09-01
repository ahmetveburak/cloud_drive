from django import forms
from martor.fields import MartorFormField


class PostForm(forms.Form):
    content = MartorFormField()


class FileCreateForm(forms.Form):
    name = forms.CharField(required=False)
    file = forms.FileField()
    is_private = forms.BooleanField(required=False)
