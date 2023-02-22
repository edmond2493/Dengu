from django import forms
from django.forms import ModelForm
from .models import Contact

# create a contact form

class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields = ["first_name", "last_name", "email", "phone", "comment"]
    # fields = "__all__"
    labels = {'first_name': "", "last_name": "", "email": "", "phone": "", "comment": ""}
    widgets = {
      "first_name": forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-6 noFont', 'placeholder': 'First Name'}),
      "last_name": forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-6 noFont', 'placeholder': 'Last Name'}),
      "email": forms.EmailInput(attrs={'class': 'form-control col-sm-12 col-md-6 noFont', 'placeholder': 'Email Address'}),
      "phone": forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-6 noFont', 'placeholder': 'Phone Number'}), 
      "comment": forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-6 noFont', 'placeholder': 'Comment'}),
    }