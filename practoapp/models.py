from django.db import models
from django.utils import timezone

# Create your models here.
class Doctor(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk) + " - " + self.title