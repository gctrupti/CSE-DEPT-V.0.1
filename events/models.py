from django.db import models
from clubs.models import Club
# Create your models here.

class Event(models.Model):
    UPCOMING = "UPCOMING"
    PAST = "PAST"

    STATUS_CHOICES = [
        (UPCOMING, "Upcoming"),
        (PAST, "Past"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UPCOMING
    )

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="events"
    )

    image = models.ImageField(
        upload_to="event_images/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} ({self.club.name})"

