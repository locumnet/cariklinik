
from django.contrib import admin
from django.urls import path, include
from backend.views import db_clinics
urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/',include('backend.urls')),
    path('backend/', db_clinics, name = "db_clinics_upload")
]
