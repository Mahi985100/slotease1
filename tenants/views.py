from django.http import HttpResponse

def home(request):
    return HttpResponse("SlotEase is running!")

def landing(request):
    return HttpResponse("Welcome to SlotEase")

def register(request):
    return HttpResponse("Register Page")

def staff_login_view(request):
    return HttpResponse("Staff Login Page")

def dashboard(request):
    return HttpResponse("Dashboard Page")

from django.http import HttpResponse

def analytics(request):
    return HttpResponse("Analytics Page")

