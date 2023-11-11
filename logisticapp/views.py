from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm, ContactForm

# Create your views her


def home(request):
    return render(request, "home.html")


def ocean_freight(request):
    return render(request, "services/ocean_freight.html")


def air_freight(request):
    return render(request, "services/air_freight.html")


def rail_freight(request):
    return render(request, "services/rail_freight.html")


def warehousing(request):
    return render(request, "services/warehousing.html")


def customs_clearance(request):
    return render(request, "services/customs_clearance.html")


def get_quote(request):
    return render(request, "get_quote.html")


def distribution(request):
    return render(request, "services/distribution.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to the home page after submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def submit_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to the home page after submission
    else:
        form = QuoteForm()

    return render(request, "get_quote.html", {"form": form})
