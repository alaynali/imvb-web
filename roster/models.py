from django.db import models

# Create your models here.
TEAM_CHOICES = (
    ('Illini 1s', 'Illini 1s'),
    ('Illini 2s', 'Illini 2s'),
    ('Illini 3s', 'Illini 3s'),
)

class CustomManager(models.Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    team = models.CharField(max_length=9, choices=TEAM_CHOICES)
    number = models.IntegerField(default=None, null=True) # this line broke the whole project
    position = models.CharField(max_length=50)
    height = models.CharField(help_text="Enter in format [feet]\'[inches]\"", default="", max_length=5)
    major = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="roster", default="profile_icon.png")

    objects = CustomManager() # assign CustomManager to model

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.team}"
    
    def delete(self, using=None, keep_parents=False):
        storage = self.image.storage

        if storage.exists(self.image.name):
            storage.delete(self.image.name)

        super().delete()
    
