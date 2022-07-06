from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Date_record, Act_record, Time_record, Detail_record, Calories_record

@csrf_exempt
def home_page(request):
    return render(request,"home.html")
    # return render(request,"result_page.html")
    # return render(request,"end_page.html")
    
    
@csrf_exempt
def time_record(request):
    if request.method == "POST":
        post_date = request.POST.get('date')
        post_time_hr_0 = request.POST.get('Select_hr_0')
        post_time_min_0 = request.POST.get('select_min_0')
        post_time_hr_1 = request.POST.get('select_hr_1')
        post_time_min_1 = request.POST.get('select_min_1')
        post_act_main = request.POST.get('act_type_main')
        post_act_sub = request.POST.get('act_type_sub')
        post_act_detail = request.POST.get('act_name')
        post_act_note = request.POST.get('act_note')
        
        post_cal_MRNG = request.POST.get('cal_MRNG')
        post_cal_NOON = request.POST.get('cal_NOON')
        post_cal_NIGHT = request.POST.get('cal_NIGHT')
        post_cal_TARGET = request.POST.get('cal_TARGET')
        if post_act_main:
            Date_record.objects.update_or_create(
                dt_date = post_date,
            # defaults = {'dt_date' : date}, 
            )

            Act_record.objects.update_or_create(
                act_main = post_act_main,
                act_sub = post_act_sub,
            )
         
            Time_record.objects.update_or_create(
                dt_date = Date_record.objects.latest('id'),
                act_act =  Act_record.objects.latest('id'),
                tm_start_time = f"{post_time_hr_0}:{post_time_min_0}:00",
                tm_end_time = f"{post_time_hr_1}:{post_time_min_1}:00",
            # tm_duration_hr = ,
            )
            if post_act_detail != '' or post_act_note != '':
                Detail_record.objects.update_or_create(
                    tm_time =  Time_record.objects.latest('id'),
                    dtl_detail = post_act_detail,
                    dtl_note = post_act_note,
                )
            return redirect('/')
        else:
            Calories_record.objects.update_or_create(
                dt_date =Date_record.objects.latest('id'),
                cal_morning = post_cal_MRNG,
                cal_noon = post_cal_NOON,
                cal_night = post_cal_NIGHT,
                cal_target = post_cal_TARGET,
                # cal_deficit = 
            )

        


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
