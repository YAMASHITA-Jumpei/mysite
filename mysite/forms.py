from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
