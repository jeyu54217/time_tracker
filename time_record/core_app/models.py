from django.db import models
from django.utils import timezone

class Date_record(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        default = 0,
        )
    dt_date = models.DateField(
        default = timezone.now,
        )

class Act_record(models.Model):
    dt_date = models.ForeignKey(
        Date_record, 
        on_delete = models.CASCADE,
        )
    act_main = models.CharField(
        max_length = 225,
        )
    act_sub = models.CharField(
        max_length = 225,
        )
    act_dtl = models.CharField(
        max_length = 225, 
        blank = True, 
        null = True, 
        default='',
        )
    act_note = models.TextField(
        blank = True, 
        null = True, 
        default='',
        )

class Time_record(models.Model):
    dt_date = models.ForeignKey(
        Date_record, 
        on_delete = models.CASCADE,
        )
    act_act = models.ForeignKey(
        Act_record, 
        on_delete = models.CASCADE,
        )
    tm_start_time = models.TimeField()
    tm_end_time = models.TimeField()
    tm_duration_hr = models.DurationField()    
    

class Calories_record(models.Model):
    dt_date = models.OneToOneField(
        Date_record,
        on_delete = models.CASCADE,
    )
    cal_morning = models.IntegerField(
        blank = True,
        null = True,
    )
    cal_noon = models.IntegerField(
        blank = True,
        null = True,
    )
    cal_night = models.IntegerField(
        blank = True,
        null = True,
    )
    cal_goal = models.IntegerField(
        blank = True,
        null = True,
    )
    cal_deficit = models.IntegerField(
        blank = True,
        null = True,
    )
    
    
    
    
    