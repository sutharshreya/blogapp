from django import forms
from .import models

# create forms for post based on this.
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','slug','content','image'] # fields need in form.