from django.db import models

# Create your models here.

class Club(models.Model):                               # Club model
    name = models.CharField(max_length=100)
    description = models.TextField()

    cover_image = models.ImageField(
        upload_to="club_covers/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="activities"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="activity_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.club.name})"
