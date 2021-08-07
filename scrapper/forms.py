
from django import forms
from .models import Post


class WebForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('Content_Type', 'Article_Title', 'Words_Per_Column',)