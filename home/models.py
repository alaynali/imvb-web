from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home')
    description = models.TextField(max_length=100)
    # hyperlink = models.URLField()

    def __str__(self):
        return f"{self.name}"
    
class Announcement(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home', blank=True)
    description = models.TextField(max_length=1000)
    button_name = models.CharField(max_length=50, blank=True)
    button_hyperlink = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True, help_text='Note: this field is REQUIRED if button name is not empty.')

    def __str__(self):
        return f"{self.name}"
