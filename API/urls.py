from django.contrib import admin
from django.urls import path
from .views import index,download_video

urlpatterns = [
    path('', index, name='index'),
    # path('download/', download_video, name='download_video'),
    # path('start-bot/', start_bot, name='start_bot'),

]