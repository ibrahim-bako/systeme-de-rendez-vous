from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Calendar(models.Model):
    """
        owner
        appointements []
        availabilities []

    """
    pass

class Appointment(models.Model):
    """
        type
        description
        valide
        user
        calendar
    """


    STATUS = [
        ("MONDAY", "Monday"),
    ]
    status = models.CharField(
        max_length=100,
        choices=STATUS,
        null=False,
        blank=False,
        verbose_name="",
    )

    start_time = models.TimeField(
        null=False,
        blank=False,
        verbose_name="",
    )

    end_time = models.TimeField(
        null=False,
        blank=False,
        verbose_name="",
    )

    date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name="",
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="appointments",
        null=False,
        blank=False,
        verbose_name="",
    )

    calendar = models.ForeignKey(
        to=Calendar,
        on_delete=models.CASCADE,
        related_name="appointments",
        null=False,
        blank=False,
        verbose_name="",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="",
    )

class Availability(models.Model):
    DAYS_OF_WEEK = [
        ("MONDAY", "Monday"),
    ]
    day_of_week = models.CharField(
        max_length=100,
        choices=DAYS_OF_WEEK,
        null=False,
        blank=False,
        verbose_name="",
    )

    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="",
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="availabilities",
        null=False,
        blank=False,
        verbose_name="",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="",
    )

class AvailabilityInterval(models.Model):

    availibility = models.ForeignKey(
        to=Availability,
        on_delete=models.CASCADE,
        related_name="intervals",
        null=False,
        blank=False,
        verbose_name="",
    )

    start_time = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name="",
    )

    end_time = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name="",
    )

class Calendar(models.Model):
    pass

class Calendar(models.Model):
    pass

