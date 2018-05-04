"""show_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from showing.views import *



urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'mainpage/$', mainpage),
    url(r'registry/$', registry),
    url(r'registry-loaded/$', registry_loaded),
    url(r'advanced-search-form$', Search.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'suppliers-table-[0123456789]{4}/$', suppliers_table),
    url(r'tables_found.json$', SearchJson.as_view()),
    #url(r'advanced-search$', advanced_search),
    #url(r'found$', found),
    #url(r'google$', createExcel, name="createExcel")
]  

