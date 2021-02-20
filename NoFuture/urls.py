"""NoFuture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import HomeView, AboutView, MusicView, CalculatorsView, YogaView, ContactView, thanks, ShippingView, \
    DesignView, DivisorsView, PrimesView, ProgrammingView
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('music/', MusicView.as_view(), name="music"),
    path('calculators/', CalculatorsView.as_view(), name="calculators"),
    path('calculators/divisors/', DivisorsView.as_view(), name="divisors"),
    path('calculators/primes/', PrimesView.as_view(), name="primes"),
    path('yoga/', YogaView.as_view(), name="yoga"),
    path('contact/', ContactView.as_view(), name="contact"),
    path("thanks/", thanks, name="thanks"),
    path('shipping/', ShippingView.as_view(), name="shipping"),
    path('design/', DesignView.as_view(), name="design"),
    path('programming/', ProgrammingView.as_view(), name="programming"),

]
