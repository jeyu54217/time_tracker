from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"home.html")
    # return render(request,"result_page.html")
    # return render(request,"end_page.html")