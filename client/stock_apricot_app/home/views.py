from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact
from server.app.api.api import Api


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def weekly_report(request):
    context = {"data": Api().get_weekly_report().get("data")}
    return render(request, 'weekly_report.html', context)


def gainers(request):
    context = {"data": Api().get_top_gainers().get("data")}
    return render(request, 'gainers.html', context)


def losers(request):
    context = {"data": Api().get_top_losers().get("data")}
    return render(request, 'losers.html', context)


def services(request):
    return HttpResponse("this is services page")
    # return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        _contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            date=datetime.now())
        _contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')
