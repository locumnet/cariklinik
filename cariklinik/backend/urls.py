from django.urls import path, re_path
from .views import ClinicView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('backend/', ClinicView.as_view(), name='clinic_view'),
]