from django.urls import path
from . import views



urlpatterns = [
    path('', views.landingPage, name="landingpage"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
]