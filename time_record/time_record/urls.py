from django.contrib import admin
from django.urls import path
from core_app import views as core_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.home_page),
    path('time_record/', core_view.time_record, name='time_record'),
    path('calories_record/', core_view.calories_record, name='calories_record'),
]
