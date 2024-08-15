from django.shortcuts import render
import yt_dlp
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
import asyncio


# Create your views here.

def video_url(video_url:str):

# URL لمقطع الفيديو الذي تريد تنزيله
    # video_url = "https://vt.tiktok.com/ZSYoBXNjd/"

    # إعدادات التنزيل
    ydl_opts = {
        'outtmpl': 'downloaded_video.mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("تم تنزيل الفيديو بنجاح!")


def index(request):
       return render (request,"index.html")


@csrf_exempt
def download_video(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_url = data['url']
        ydl_opts = {
            'outtmpl': 'downloaded_video.mp4',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return JsonResponse({"status": "success", "message": "تم تنزيل الفيديو بنجاح!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method."})











