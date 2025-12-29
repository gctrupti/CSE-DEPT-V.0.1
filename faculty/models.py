from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='faculty_profiles/', null=True, blank=True)

    def __str__(self):
        return self.name