from django.contrib import admin
from django.urls import path
from home import views
from django.shortcuts import render

urlpatterns = [
    path("", views.base, name='base'),
    path("frontend.html", views.frontend, name='home'),
    path("base.html", views.base, name='index'),
    path("aboutus.html", views.aboutus, name='aboutus'),
    # path("services", views.services, name='services'),  # Uncomment if you need it
    path("signin.html", views.signin_view, name='signin'),  # Changed 'Sign In' to 'signin'
    path("signup.html", views.signup_view, name='signup'),  # Kept 'signup' for the signup page
    path("availablecycles.html", views.availablecycles, name='availablecycles'),
    path("contactus.html", views.contactus, name='contactus'),
    path("wallet.html", views.wallet, name='wallet'),
    path("PaymentGateway.html", views.PaymentGateway, name="payment_gateway"),
    path('signup/', views.signin_view, name='signin_form'),  # Renamed to 'signin_form' for uniqueness
    # Ensure you only have one 'signup' name
    path('addcycle.html', views.addabicycle, name='addabicycle'),
    path('previousbookings.html', views.previousbookings, name='previousbookings'),
    path('addabicycle.html', views.addabicycle, name='addabicycle'),
    path('changelocation.html', views.changedestination, name='changelocation'),
    path('viewtransactions.html', views.viewtransactions, name='viewtransactions'),
]
