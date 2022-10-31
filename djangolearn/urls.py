"""djangolearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from djangolearn.views import home_view # from .views import home_view
from firstapp. views import show_data, create_entry

urlpatterns = [
    path('admin/', admin.site.urls), # default
    path('', home_view),
    path('user/', show_data),
    path('user/create', create_entry),
    path('user/<int:id>/', show_data) # re_path also used in to make using Regular Expressions which is complex
]

# order in urlpatterns dose matter # make nates in .md file
# 1. user/    2. user/anything    3. user/<datatype:variablename>