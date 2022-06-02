"""anketa URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('', main, name='main'),
    path('forms/<int:pk>/', getForm, name='getForm'),
    path('admin/', adminPanel, name='adminPanel'),
    path('admin/search_datas/', search_datas, name='search_datas'),
    path('admin/api_datas/', apiDatas, name='api_datas'),
    path('admin/change_api_checkbox/', changeApiCheckbox, name='apiDatas'),
    path('admin/list_datas/<int:pk>/', listDatas, name='listDatas'),
    path('admin/data/<int:pk>/', getData, name='getData'),
    path('admin/list_datas/<int:pk>/delete/', deleteData, name='deleteData'),
    path('admin/form/<int:pk>', deleteForm, name='deleteForm'),
    path('admin/form/add', addForm, name='addForm'),
    path('change_checker_of_data/', changeCheckerOfData, name='changeCheckerOfData'),
    path('login/', login_profile, name='login'),
    path('logout/', logout_profile, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
