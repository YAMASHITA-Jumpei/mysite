from django import forms


class FileUploadForm(forms.Form):
    upload = forms.FileField()
