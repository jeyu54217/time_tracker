from django.contrib import admin
from django.urls import path
from core_app import views as core_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.home_page),
]
