from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    # team = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="This field is optional.")
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    result_text = models.TextField(blank=True)
    result_link = models.URLField(blank=True, help_text="Paste a link to a results page (e.g. MIVA bracket).")
    
    # tournament_id = models.CharField(editable=False, default=str(start_date), max_length=10)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # self.id = f"{self.start_date.strftime('%m%d%y')}"
        if self.end_date:
            return f"{self.name} | {self.start_date.strftime('%m/%d/%y')}-{self.end_date.strftime('%m/%d/%y')}"
        else:
            return f"{self.name} | {self.start_date.strftime('%m/%d/%y')}" 
        
    def get_absolute_url(self):
        return reverse("schedule:detail", kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.updated = timezone.now()
    #     return super(Tournament, self).save(*args, **kwargs)

class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.end_date:
            return f"{self.name} | {self.start_date.strftime('%m/%d/%y')} - {self.end_date.strftime('%m/%d/%y')}"
        else:
            return f"{self.name} | {self.start_date.strftime('%m/%d/%y')}" 
    