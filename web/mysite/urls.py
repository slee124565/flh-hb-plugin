"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .views import SiteResetAPI, SiteConfigAPI, AngularTemplateView

urlpatterns = [
    
    #url(r'^admin/', admin.site.urls),
    
    #url(r'^$', HomePageView.as_view(), name='home'),
    
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^views/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view()),

    url(r'^webapp/api/config$', csrf_exempt(SiteConfigAPI.as_view()), name='sitconfig'),
    url(r'^webapp/api/reset', csrf_exempt(SiteResetAPI.as_view()), name='sitreset'),

]
