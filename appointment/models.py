from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Calendar(models.Model):
    """
        owner
        appointements []
        availabilities []
    """
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="",
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="",
    )

    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="",
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="",
    )

    unlimited_period = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name="",
    )

    period_start_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="",
    )

    period_end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="",
    )

    appointments_limit_per_day = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="",
    )

    SLOT_INCREMENT_IN_MINUTES = [
        (15, "15 minutes"),
        (30, "30 minutes"),
        (60, "1 hour"),
    ]
    slot_increment_in_minutes = models.IntegerField(
        choices=SLOT_INCREMENT_IN_MINUTES,
        default=30,
        null=False,
        blank=False,
        verbose_name="",
    )

    enppointment_duration_in_minutes = models.IntegerField(
        default=30,
        null=False,
        blank=False,
        verbose_name="",
    )

    active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name="",
    )

    thumbnail = models.ImageField(
        upload_to=None, 
        height_field=200,
        width_field=150,
        max_length=100,
        default=True,
        null=False,
        blank=False,
        verbose_name="",
    )

    created_at = models.DateTimeField(
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
        null=True,
        blank=True,
        verbose_name="",
    )

    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="",
    )

    calendar = models.ForeignKey(
        to=Calendar,
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


class Appointment(models.Model):
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

    date = models.DateField(
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


class Attendee(models.Model):
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="",
    )

    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="",
    )

    email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="",
    )

    phone_number = models.CharField()

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        related_name="attendees",
        null=True,
        blank=True,
    )

    appointment = models.ForeignKey(
        to=Appointment,
        on_delete=models.SET_NULL,
        related_name="attendees",
        null=True,
        blank=True,
    )