from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.CharField(null=True, max_length=1000)
    producer = models.CharField(null=False, max_length=100)
    duration = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.title