#-*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include

#admin site customizations
admin.site.site_header = "IIIT-L Lucknow Library Admininstration"
admin.site.site_title = "Library-IIIT-L"
admin.site.index_title = "Welcome to IIIT-L Library"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
]

# To redirect to base urls of our application
from django.views.generic import RedirectView 
urlpatterns += [
    path('', RedirectView.as_view(url = '/catalog/'))
]
