from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from pytube import YouTube


@csrf_exempt
def home(request):
    if request.method == 'POST':
        data = {}
        print(request.POST)
        if request.POST["changer_b"] == "V":
            my_video = YouTube(request.POST["url"])
            data = {
                "title_song" : my_video.title,
                "is_search" : True,
                "image" : my_video.thumbnail_url,
                "url_load" : request.POST["url"]
            }
        else :
            my_video = YouTube(request.POST["url"])
            my_video.streams.first().download()
            data = {
                "is_download" : True,
                "is_search" : False,
            }
        return render(request , "home.html" ,data)
    else :
        return render(request , 'home.html')