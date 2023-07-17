from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    def __str__(self):
        return f"{self.name} | {self.start_date.strftime('%m/%d/%y')}-{self.end_date.strftime('%m/%d/%y')}"
