from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Date_record, Act_record, Time_record, Detail_record, Calories_record
# from core_app.models import Date_record, Act_record, Time_record, Detail_record, Calories_record
from datetime import datetime, timezone, timedelta

TIME_ZONE = timezone(timedelta(hours=+8))
TODAY_DATE = datetime.now(TIME_ZONE).strftime('%Y-%m-%d')


@csrf_exempt
def home_page(request):
    """Targets:
      1. To present today's calorie record on the homepage if exist (for duplicate typing prevention).
      2. Rendering time_results for datatable.
    """
    today_date_id = Date_record.objects.get(dt_date = TODAY_DATE).id \
        if Date_record.objects.filter(dt_date = TODAY_DATE).exists() \
        else False
    today_cal_obj = Calories_record.objects.get(cal_date = today_date_id) \
        if today_date_id and Calories_record.objects.filter(cal_date = today_date_id).exists() \
        else False
    time_results = Time_record.objects.all() \
        if Time_record.objects.all().exists() \
        else False
    
    content = {}
    if today_cal_obj and time_results:
        content.update({
            'time_results' : time_results, 
            'today_cal_obj' : today_cal_obj, 
            })
    elif today_cal_obj and not time_results:
        content.update({
            'today_cal_obj' : today_cal_obj, 
            })
    elif time_results and not today_cal_obj:
        content.update({
            'time_results' : time_results, 
            })
    else:
        pass
    
    return render(request, "home.html", content)

@csrf_exempt
def time_record(request):
    if request.method == "POST":
        post_date = request.POST.get('date')
        post_time_hr_s = request.POST.get('Select_hr_0')
        post_time_min_s = request.POST.get('select_min_0')
        post_time_hr_e = request.POST.get('select_hr_1')
        post_time_min_e = request.POST.get('select_min_1')
        post_act_main = request.POST.get('act_type_main')
        post_act_sub = request.POST.get('act_type_sub')
        post_act_detail = request.POST.get('act_name')
        post_act_note = request.POST.get('act_note')

        if post_time_hr_s:
            Date_record.objects.update_or_create(
                dt_date = post_date,
            )
            Act_record.objects.update_or_create(
                # if not set defaults : filters = defaults
                act_main = post_act_main,
                act_sub = post_act_sub,
            )
            Time_record.objects.update_or_create(
                # filter on the unique value of below fields
                tm_date = Date_record.objects.latest('id'),
                tm_start_time = f"{post_time_hr_s}:{post_time_min_s}:00",
                tm_end_time = f"{post_time_hr_e}:{post_time_min_e}:00",
                # update these fields, or create a new object with these values
                defaults = {
                    'tm_date' : Date_record.objects.latest('id'),
                    'tm_act': Act_record.objects.latest('id'),
                    'tm_start_time': f"{post_time_hr_s}:{post_time_min_s}:00",
                    'tm_end_time': f"{post_time_hr_e}:{post_time_min_e}:00",
                    }
            # tm_duration_hr = ,
            )
            if post_act_detail != '' or post_act_note != '':
                Detail_record.objects.update_or_create(
                    # filer by selected time record, not by the latest one
                    dtl_time =  Time_record.objects.latest('id'),
                    defaults = {
                        'dtl_detail' : post_act_detail,
                        'dtl_note': post_act_note,
                        }
                    )
            return redirect('/')
        else:
            pass

@csrf_exempt
def calories_record(request):
    if request.method == "POST":
        post_date = request.POST.get('date')
        post_cal_MRNG = request.POST.get('cal_MRNG')
        post_cal_NOON = request.POST.get('cal_NOON')
        post_cal_NIGHT = request.POST.get('cal_NIGHT')
        post_cal_TARGET = request.POST.get('cal_TARGET')
        post_cal_DIFICITE = request.POST.get('cal_DEFICITE')
        Date_record.objects.update_or_create(
                dt_date = post_date,
            )
        # 寫入用obj
        Calories_record.objects.update_or_create(
                cal_date = Date_record.objects.get(dt_date = post_date),
                defaults = {
                    'cal_date' : Date_record.objects.get(dt_date = post_date),
                    'cal_morning' : post_cal_MRNG,
                    'cal_noon': post_cal_NOON,
                    'cal_night': post_cal_NIGHT,
                    'cal_target': post_cal_TARGET,
                    'cal_deficit': post_cal_DIFICITE,
                    }
                )
        return redirect('/')

def download_csv(request):
    '''
    User Specs :
      1. select box: 
         1) time act records
         2) calories 
         3) both of all
      2. select Date range:
      3. querry to Pandas DataFrame
      4. DataFrame to csv
      5. download by browser
    '''
    pass
