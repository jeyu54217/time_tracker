from django.db import models
from django.utils import timezone

class Date_record(models.Model):
    dt_date = models.DateField(
        default = timezone.now,
        )

class Act_record(models.Model):
    act_main = models.CharField(
        max_length = 225,
        )
    act_sub = models.CharField(
        max_length = 225,
        )
    
class Time_record(models.Model):
    tm_date = models.ForeignKey(
        Date_record, 
        on_delete = models.CASCADE,
        )
    tm_act = models.ForeignKey(
        Act_record, 
        on_delete = models.CASCADE,
        )
    tm_start_time = models.TimeField()
    tm_end_time = models.TimeField()
    # tm_duration_hr = models.DurationField()    
    
    
class Detail_record(models.Model):
    dtl_time = models.OneToOneField(
        Time_record,
        on_delete = models.CASCADE,
    )
    dtl_detail = models.CharField(
        max_length = 225, 
        blank = True, 
        null = True, 
        default='',
        )
    dtl_note = models.TextField(
        blank = True, 
        null = True, 
        default='',
        )

class Calories_record(models.Model):
    cal_date = models.OneToOneField(
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
    cal_target = models.IntegerField(
        blank = True,
        null = True,
    )
    cal_deficit = models.IntegerField(
        blank = True,
        null = True,
    )
    
    
    
    
    