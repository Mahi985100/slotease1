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

def service_list(request):
    from django.http import HttpResponse
    return HttpResponse("Service List")

def service_edit(request):
    return render(request, "tenants/service_form.html")

def service_delete(request, pk):
    if request.method == "POST":
        # example logic (adjust to your model)
        # Service.objects.get(id=pk).delete()
        return redirect("service_list")

    return render(request, "tenants/service_confirm_delete.html")

