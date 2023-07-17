from django.db import models

# Create your models here.
TEAM_CHOICES = (
    ('Illini 1s', 'Illini 1s'),
    ('Illini 1s', 'Illini 2s'),
    ('Illini 1s', 'Illini 3s'),
)

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    team = models.CharField(max_length=9, choices=TEAM_CHOICES)
    position = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.team}"