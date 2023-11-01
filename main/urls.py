"""
URL configuration for resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
    path("thank-you/", views.ThankYouView.as_view()),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]