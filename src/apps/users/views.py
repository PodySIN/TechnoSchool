from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def registration_page(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/registration.html")

