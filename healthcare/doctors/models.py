from django.db import models
from django.conf import settings

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"

    class Meta:
        ordering = ['-created_at']