from django.db import models
from django.utils import timezone

class Date_record(models.Model):
    start_time = models.DateField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )

class Time_records(models.Model):
    start_time = models.TimeField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )
    
    end_time = models.TimeField(
        blank = True, 
        null = False, 
        )
    
    act_type_1 = models.CharField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )
    
    act_type_2 = models.CharField(
        max_length = 255, 
        blank = True, 
        null = True, 
        )
    
    act_name = models.CharField(
        max_length = 255, 
        blank = True, 
        null = True, 
        )
    
    act_note = models.TextField(
        blank = True, 
        null = True, 
        default = "",
        )


class Calories_records(models.Model):
    start_time = models.IntegerField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )