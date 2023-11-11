from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ocean-freight", views.ocean_freight, name="ocean_freight"),
    path("air-freight", views.air_freight, name="air_freight"),
    path("rail-freight", views.rail_freight, name="rail_freight"),
    path("warehousing", views.warehousing, name="warehousing"),
    path("customs-clearance", views.customs_clearance, name="customs_clearance"),
    path("distribution", views.distribution, name="distribution"),
    path("about-us", views.about, name="about_us"),
    path("contact", views.contact, name="contact"),
    path("getQuote", views.submit_quote, name="getquote"),
]
