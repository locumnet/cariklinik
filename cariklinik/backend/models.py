from django.db import models
from django.contrib.gis.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, unique=True)
    postcode = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    location = models.PointField(null=False, blank=False, srid=4326, verbose_name = 'Location')
    status = models.CharField(max_length=10)
    institution = models.CharField(max_length=10)
    jenis = models.CharField(max_length=50)
    rating = models.IntegerField()
    service = models.CharField(max_length=250)
    panel = models.CharField(max_length=250)
    image = models.ImageField(upload_to='clinic_image/', blank=True)
    hour = models.TimeField() #need correction in format

    def __str__(self):
        return self.name






