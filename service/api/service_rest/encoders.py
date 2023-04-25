from common.json import ModelEncoder

from .models import AutomobileVO, CustomerVO, Technician, Appointment, Status


class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = ["id", "vin"]


class CustomerVOEncoder(ModelEncoder):
    model = CustomerVO
    properties = ["id", "first_name", "last_name"]


class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = ["id", "first_name", "last_name", "employee_id"]


class StatusEncoder(ModelEncoder):
    model = Status
    properties = ["id", "name"]


class AppointmentEncoder(ModelEncoder):
    model = Appointment
    properties = [
        "id",
        "date_time",
        "reason",
        "status",
        "vin",
        "customer",
        "technician",
    ]
    encoders = {
        "vin": AutomobileVOEncoder(),
        "customer": CustomerVOEncoder(),
        "status": StatusEncoder(),
    }

    # TODO: may need to get more data
