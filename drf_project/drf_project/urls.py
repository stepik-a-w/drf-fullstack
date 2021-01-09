"""drf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

import sample.views as sample_views
import api.views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sample_views.index_view, name='main'),

    path('api/get-username/', api_views.get_username),
    path('api/get-options/', api_views.get_options),
    path('api/add-request/', api_views.add_request),

]

