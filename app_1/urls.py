from django.urls import re_path

from app_1.views import IndexView, time_api_call, car_price_api

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name="index"),
    re_path(r'^time_api$', time_api_call, name="time_api"),
    re_path(r'^car_api$', car_price_api, name="car_api"),
]