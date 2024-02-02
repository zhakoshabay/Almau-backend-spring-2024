from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(null=False, max_length=100)
    text = models.CharField(null=True, max_length=1000)
    author = models.CharField(null=False, max_length=100)

    def __str__(self) -> str:
        return self.title