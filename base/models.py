from django.db import models   #This is essential because it provides the base class (models.model).

# Create your models here.
class Topic(models.Model):     # This line creates a table named "Topic".
    tech_name = models.CharField(max_length=50, null=True, blank=True)
    tech_description = models.TextField(null=True)

    def __str__(self):                # This defines a special method called __str__.This method is used to provide ac human readable string of the topic object.
        return f"{self.tech_name}"    # This line return the value of the tech name field so we can print topic it display th evalue of tech name.

class contactEnquiry(models.Model):   # It inhrits from models.Model, making it a djang model. This will create a table named contact enquiry in the database.
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    subject=models.TextField()


