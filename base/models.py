from django.db import models

# Create your models here.
class Topic(models.Model):
    tech_name = models.CharField(max_length=50, null=True, blank=True)
    tech_description = models.TextField(null=True)

    def __str__(self):
        return f"{self.tech_name}"

class contactEnquiry(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    subject=models.TextField()


