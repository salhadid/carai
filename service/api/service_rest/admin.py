from django.contrib import admin

from .models import Technician, Status, Appointment, AutomobileVO


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(AutomobileVO)
class AutomobileVOAdmin(admin.ModelAdmin):
    pass
