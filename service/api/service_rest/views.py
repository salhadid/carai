from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from .encoders import (
    AutomobileVOEncoder,
    CustomerVOEncoder,
    TechnicianEncoder,
    StatusEncoder,
    AppointmentEncoder,
)

from .models import CustomerVO, AutomobileVO, Technician, Status, Appointment

# Create your views here.
