from django.db import models

# Create your models here.
class Patients(models.Model):
    full_name = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)