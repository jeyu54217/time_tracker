from django.db import models
from django.contrib.auth.models import User

class Date(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f'{self.date}'
class Time(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_duration = models.DurationField()  
    act_type = models.CharField(max_length=100)
    act_name = models.CharField(max_length=100)
    notes = models.TextField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE) 
    
    # Automatically calculate the time_duration when saving
    def save(self, *args, **kwargs):
        self.time_duration = self.end_time - self.start_time
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.date},{self.start_time}-{self.end_time},{self.act_type},{self.act_name},{self.notes}"
    
    class Meta:
        ordering = ['date', 'start_time']

class Act_type(models.Model):
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f'User: {self.user} Type: {self.type}'
    
class Act_name(models.Model):
    name = models.CharField(max_length=100)
    act_type = models.ForeignKey(Act_type, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f'{self.act_type} - {self.name}'