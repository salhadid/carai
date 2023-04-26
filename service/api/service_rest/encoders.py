from common.json import ModelEncoder

from .models import AutomobileVO, Technician, Appointment


class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = ["id", "vin"]


class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = ["id", "first_name", "last_name", "employee_id"]


class AppointmentEncoder(ModelEncoder):
    model = Appointment
    properties = [
        "id",
        "appt_date",
        "appt_time",
        "reason",
        "vin",
        "customer",
        "technician",
        "vip_status",
    ]
    encoders = {
        "technician": TechnicianEncoder(),
    }

    def get_extra_data(self, o):
        return {
            "status": o.status.name,
            "appt_date": str(o.appt_date),
            "appt_time": str(o.appt_time),
        }
