from django.shortcuts import render
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
        act_type_main = request.POST.get('act_type_main')
        act_type_sub = request.POST.get('act_type_sub')
        act_name = request.POST.get('act_name')
        act_note = request.POST.get('act_note')
        
        Date_record.objects.update_or_create(
            dt_date = date,
            defaults = {'dt_date' : date}, 
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
            dt_date = date,
            act_main = act_type_main,
            act_sub = act_type_sub,
            # act_dtl =
            # act_note =
        )
        
        # Time_record.objects.update_or_create(
        #     dt_date = date,
        #     act_act
        #     tm_start_time
        #     tm_end_time
        #     tm_duration_hr
        # )
        
        




@csrf_exempt
def calories_record(request):
    return render(request,"home.html")
