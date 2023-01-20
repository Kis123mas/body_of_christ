from django.shortcuts import render
from django.http import HttpResponse

# landing page
def landingPage(request):
    return render(request, 'landapp/landingpage.html')


# login page
def loginPage(request):
    return render(request, 'landapp/login.html')


# register page
def registerPage(request):
    return render(request, 'landapp/register.html')


# dashboard page
def dashboardPage(request):
    return render(request, 'landapp/dashboard.html')