from django.urls import path
from .views import (Dashboard_view
                    )

urlpatterns = [
    path('get/', Dashboard_view.as_view(), name='dashboard_get'),
    path('post/', Dashboard_view.as_view(), name='dashboard_post'),
    ]
