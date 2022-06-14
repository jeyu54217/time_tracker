from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_page(request):
    return render(request,"home.html")
    # return render(request,"result_page.html")
    # return render(request,"end_page.html")