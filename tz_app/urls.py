from django.urls import path
from tz_app import views

app_name = 'tz_app'
urlpatterns = [
    #homepage
    path('', views.start, name='start'),
]