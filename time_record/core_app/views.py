from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_page(request):
    return render(request,"home.html")
    # return render(request,"result_page.html")
    # return render(request,"end_page.html")
    
    
@csrf_exempt
def time_record(request):
    return render(request,"home.html")

@csrf_exempt
def calories_record(request):
    return render(request,"home.html")
