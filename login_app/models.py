from django.db import models

# Create your models here.
class Persons(models.Model):
    person_name = models.CharField(max_length=10)
    person_email = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name