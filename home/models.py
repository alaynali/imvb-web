from django.db import models

# Create your models here.

class Announcement(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField(max_length=500)
    hyperlink = models.URLField()

    def __str__(self):
        return f"{self.name}"
