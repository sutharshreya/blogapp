from django import forms
from .import models

# create form for contact_us.
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = "__all__"  # fields required in form.