from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home')
    description = models.TextField(max_length=200)
    hyperlink = models.URLField()

    def __str__(self):
        return f"{self.name}"
    
class Announcement(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home', blank=True)
    description = models.TextField(max_length=1000)
    button_name = models.TextField(max_length=50)
    button_hyperlink = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
