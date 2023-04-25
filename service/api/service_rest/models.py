from django.db import models
from django.urls import reverse


class AutomobileVO(models.Model):
    vin = models.CharField(max_length=17, unique=True)


class Technician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ("id",)


class Status(models.Model):
    """
    The Status model provides a status to an Appointment, which
    can be CREATED, CANCELED, or FINISHED.

    Status is a Value Object and, therefore, does not have a
    direct URL to view it.
    """

    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)  # Default ordering for Status
        verbose_name_plural = "statuses"  # Fix the pluralization


class Appointment(models.Model):
    @classmethod
    def create(cls, **kwargs):
        # set status
        kwargs["status"] = Status.objects.get(name="CREATED")

        # get vip status
        inventory_vins = AutomobileVO.objects.all()
        vins = [inv_vin.vin for inv_vin in inventory_vins]
        service_vin = kwargs["vin"]
        if service_vin in vins:
            kwargs["vip_status"] = True
        else:
            kwargs["vip_status"] = False

        # create the appointment
        appointment = cls(**kwargs)
        appointment.save()
        return appointment

    created = models.DateTimeField(auto_now_add=True)
    date_time = models.CharField(
        max_length=25
    )  # use charfield to test initial endpoints
    reason = models.CharField(max_length=200)
    vin = models.CharField(max_length=17, unique=True)
    customer = models.CharField(max_length=200)
    vip_status = models.BooleanField(default=False)
    technician = models.ForeignKey(
        Technician,
        related_name="appointments",
        on_delete=models.PROTECT,
    )
    status = models.ForeignKey(
        Status,
        related_name="appointments",
        on_delete=models.PROTECT,
    )

    def get_date(self):
        """Get the date from the date_time attribute in the format mm/dd/yyyy"""
        pass

    def get_time(self):
        """Get the time from the date_time attribute in the format HH:mm ss"""
        pass

    def cancel(self):
        status = Status.objects.get(name="CANCELED")
        self.status = status
        self.save()

    def finish(self):
        status = Status.objects.get(name="FINISHED")
        self.status = status
        self.save()

    def get_api_url(self):
        return reverse("api_show_appointment", kwargs={"pk": self.pk})

    def __str__(self):
        return self.vin

    class Meta:
        ordering = ("date_time",)
