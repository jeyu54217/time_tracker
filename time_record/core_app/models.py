from django.db import models
from django.utils import timezone

class Time_records(models.Model):
    start_time = models.CharField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )
    end_time = models.TextField(
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
        blank = False, 
        null = False, 
        )
    act_note = models.TextField(
        blank = True, 
        null = True, 
        default = "",
        )
