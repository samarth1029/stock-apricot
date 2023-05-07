from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("weekly_report", views.weekly_report, name="weekly_report"),
    path("gainers", views.gainers, name="gainers"),
    path("losers", views.losers, name="losers"),
]
