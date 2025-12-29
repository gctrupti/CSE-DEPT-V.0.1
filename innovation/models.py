from django.db import models
from faculty.models import Faculty
# Create your models here.

class InnovationContribution(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='innovations')
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    proof_image = models.ImageField(upload_to='innovation_proofs/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.faculty.name} ({self.year})"