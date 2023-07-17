from django.db import models
from django.utils import timezone

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    # team = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    tournament_id = ''
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.tournament_id = f"{self.start_date.strftime('%m%d%y')}"
        return f"{self.name} | {self.start_date.strftime('%m/%d/%y')}-{self.end_date.strftime('%m/%d/%y')}"
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.updated = timezone.now()
    #     return super(Tournament, self).save(*args, **kwargs)
