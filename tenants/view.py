from django.http import HttpResponse

def home(request):
    return HttpResponse("SlotEase is running!")
