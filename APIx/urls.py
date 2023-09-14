from django.conf.urls import url
from django.urls import path
from APIx import views
from APIx.views import accountApi

urlpatterns = [
     url(r'^account$',views.accountApi),
     path('account/<int:id>', accountApi, name='account_api'),
     url(r'^account/',views.accountApi),
     url(r'^account',views.accountApi),
]
