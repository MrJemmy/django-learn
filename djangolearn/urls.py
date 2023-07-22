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
from django.urls import path, include # include for routing app directly to other App's view

from djangolearn.views import home_view, NewHomeView  # from .views import home_view
from firstapp.views import (
    show_data, create_entry, show_data_slug
)
from accounts.views import (
    login_view, logout_view, register_view
)
from django.conf import settings
from django.conf.urls.static import static

# try To keep it in Alphabetical order
urlpatterns = [
    path('admin/', admin.site.urls), # default
    # path('', NewHomeView.as_view()), # for class base view
    path('', home_view),
    path('drf/', include('restframeworklearn.urls')),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('user/', include('firstapp.urls')),
    path('ecommerce/', include('store.urls')), # re_path also used in to make using Regular Expressions which is complex
    path('recipes/', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this ill allowed to create automatic URL to image

# order in urlpatterns dose matter # make nates in .md file
# 1. user/    2. user/anything    3. user/<datatype:variablename>