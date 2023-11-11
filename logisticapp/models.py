from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quote(models.Model):
    service_choices = [
        ("ocean", "Ocean Freight"),
        ("air", "Air Freight"),
        ("rail", "Rail Freight"),
        ("warehousing", "Warehousing"),
        ("customs", "Customs Clearance"),
        ("distribution", "Distribution"),
    ]

    service = models.CharField(max_length=20, choices=service_choices)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    forwarded_to = models.ManyToManyField(
        User, related_name="forwarded_quotes", blank=True
    )

    is_forwarded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}  {self.service}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=10)
    forwarded_to = models.ManyToManyField(
        User, related_name="contacts_forwarded_to", blank=True
    )

    def __str__(self):
        return self.name
