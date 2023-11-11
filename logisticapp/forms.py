from django import forms
from .models import *


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            "service",
            "name",
            "phone_number",
            "email",
            "company_name",
            "industry",
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
