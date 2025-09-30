from django.shortcuts import render


def login_page(request):
    return render(request, "pages/auth/login.html")

def register_page(request):
    return render(request, "pages/auth/register.html")

def imprint_page(request):
    return render(request, "pages/imprint/index.html")

def privacy_page(request):
    return render(request, "pages/privacy/index.html")

def dashboard_page(request):
    return render(request, "pages/dashboard/index.html")

