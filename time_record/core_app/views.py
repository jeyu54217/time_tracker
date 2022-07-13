from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Date_record, Act_record, Time_record, Detail_record, Calories_record

@csrf_exempt
def home_page(request):
    content = {
        # 'time_record_set' : ,
        'current_cal_obj' : Calories_record.objects.latest('dt_date'),
        }
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
                dt_date = Date_record.objects.latest('id'),
                tm_start_time = f"{post_time_hr_s}:{post_time_min_s}:00",
                tm_end_time = f"{post_time_hr_e}:{post_time_min_e}:00",
                # update these fields, or create a new object with these values
                defaults = {
                    'dt_date' : Date_record.objects.latest('id'),
                    'act_act': Act_record.objects.latest('id'),
                    'tm_start_time': f"{post_time_hr_s}:{post_time_min_s}:00",
                    'tm_end_time': f"{post_time_hr_e}:{post_time_min_e}:00",
                    }
            # tm_duration_hr = ,
            )
            if post_act_detail != '' or post_act_note != '':
                Detail_record.objects.update_or_create(
                    # filer by selected time record, not by the latest one
                    tm_time =  Time_record.objects.latest('id'),
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
                dt_date = Date_record.objects.get(dt_date = post_date),
                defaults = {
                    'dt_date' : Date_record.objects.get(dt_date = post_date),
                    'cal_morning' : post_cal_MRNG,
                    'cal_noon': post_cal_NOON,
                    'cal_night': post_cal_NIGHT,
                    'cal_target': post_cal_TARGET,
                    'cal_deficit': post_cal_DIFICITE,
                    }
                )
        return redirect('/')

