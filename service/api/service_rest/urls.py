from django.urls import path

# from .views import
from .views import api_technician, api_technicians

urlpatterns = [
    path("technicians/", api_technicians, name="api_technicians"),
    path("technicians/<int:pk>/", api_technician, name="api_technician"),
]
