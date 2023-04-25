from django.shortcuts import get_object_or_404
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


# technician views


@require_http_methods(["GET", "POST"])
def api_technicians(request):
    """
    API endpoint to get a list of Technician objects or create a single Technician
    object.

    GET:
    Returns a dictionary with a single key "technicians" which is a list of technician
    resources.

    {
        "technicians": [
            {
                "first_name": (str) Technician's first name,
                "last_name": (str) Technician's last name,
                "employee_id": (str) Technician's employee id,
            },
            ...
        ]
    }

    POST:
    Creates a technician resource and returns its details.
    {
        "first_name": (str) Technician's first name,
        "last_name": (str) Technician's last name,
        "employee_id": (str) Technician's employee id (must be unique)
    }
    """
    if request.method == "GET":
        technicians = Technician.objects.all()
        return JsonResponse(
            {"technicians": technicians},
            encoder=TechnicianEncoder,
        )
    else:
        # TODO: consider adding logic here to check/handle employee_id
        content = json.loads(request.body)
        technician = Technician.objects.create(**content)
        return JsonResponse(
            technician,
            encoder=TechnicianEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE"])
def api_technician(request, pk):
    """
    Returns the details for a single Technician resource specified by the pk parameter.
    Can also delete the specified technician resource.

    Returns a dictionary with a single key "technician" with the specific technician's
    information.

    GET:
    {
        "technician": {
                "id": primary key (pk),
                "first_name": (str) Technician's first name,
                "last_name": (str) Technician's last name,
                "employee_id": (str) Technician's employee id,
            }
    }
    """
    if request.method == "DELETE":
        technician = get_object_or_404(Technician, id=pk)
        technician.delete()
        message = f"Deleted technician: {technician.first_name} {technician.last_name}"
        return JsonResponse({"message": message})
    else:
        # GET response for individual technician id
        technician = get_object_or_404(Technician, id=pk)
        return JsonResponse(
            {"technician": technician}, encoder=TechnicianEncoder, safe=False
        )


# appointment views
