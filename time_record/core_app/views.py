from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Date_record, Act_record, Time_record, Calories_record

@csrf_exempt
def home_page(request):
    return render(request,"home.html")
    # return render(request,"result_page.html")
    # return render(request,"end_page.html")
    
    
@csrf_exempt
def time_record(request):
    if request.method == "POST":
        date = request.POST.get('date')
        time_hr_0 = request.POST.get('Select_hr_0')
        time_min_0 = request.POST.get('select_min_0')
        time_hr_1 = request.POST.get('select_hr_1')
        time_min_1 = request.POST.get('select_min_1')
        act_main = request.POST.get('act_type_main')
        act_sub = request.POST.get('act_type_sub')
        act_name = request.POST.get('act_name')
        act_note = request.POST.get('act_note')
        
        Date_record.objects.update_or_create(
            dt_date = date,
            # defaults = {'dt_date' : date}, 
            )

        
        # Time_record.objects.update_or_create(
        #     dt_date_id = Date_record.objects.get,
        #     act_act_id = ,
        #     tm_start_time = ,
        #     tm_end_time = ,
        #     tm_duration_hr = ,
        #     defaults = {'dt_date' : date}, 
        #     )

        Act_record.objects.update_or_create(
            act_main = act_main,
            act_sub = act_sub,
        )
         
        Time_record.objects.update_or_create(
            dt_date = Date_record.objects.latest('id'),
            act_act =  Act_record.objects.latest('id'),
            tm_start_time = f"{time_hr_0}:{time_min_0}:00",
            tm_end_time = f"{time_hr_1}:{time_min_1}:00",
            # tm_duration_hr = ,
        )
        return redirect('/')
        



    
# class Time_record(models.Model):
#     dt_date = models.ForeignKey(
#         Date_record, 
#         on_delete = models.CASCADE,
#         )
#     act_act = models.ForeignKey(
#         Act_record, 
#         on_delete = models.CASCADE,
#         )
#     tm_start_time = models.TimeField()
#     tm_end_time = models.TimeField()
#     tm_duration_hr = models.DurationField()    
    
# class Detail_record(models.Model):
#     tm_time = models.OneToOneField(
#         Time_record,
#         on_delete = models.CASCADE,
#     )
#     dtl_detail = models.CharField(
#         max_length = 225, 
#         blank = True, 
#         null = True, 
#         default='',
#         )
#     dtl_note = models.TextField(
#         blank = True, 
#         null = True, 
#         default='',
#         )

# class Calories_record(models.Model):
#     dt_date = models.OneToOneField(
#         Date_record,
#         on_delete = models.CASCADE,
#     )
#     cal_morning = models.IntegerField(
#         blank = True,
#         null = True,
#     )
#     cal_noon = models.IntegerField(
#         blank = True,
#         null = True,
#     )
#     cal_night = models.IntegerField(
#         blank = True,
#         null = True,
#     )
#     cal_target = models.IntegerField(
#         blank = True,
#         null = True,
#     )
#     cal_deficit = models.IntegerField(
#         blank = True,
#         null = True,
#     )
    




@csrf_exempt
def calories_record(request):
    return render(request,"home.html")
