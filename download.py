from pytube import YouTube
from pytube import Channel
import os, string, re

c = Channel('https://www.youtube.com/channel/UCszy2T-XzqrpJ53qXWuzerw/videos')

print(c.channel_name)

downloadable_video_arr = []
local_video_arr = []

decision = input("1: For Download only audio\n2:For download 360p\n3:For download 480p\n4:For download 720p ")

for video in c.videos:
    # Only audio's will be downloaded.
    print(video.title + "\n")
    #os.mkdir("/home/emre/avcioglu_vids")
    if decision == "1":
        video.streams.get_audio_only().download('/home/emre/avcioglu_vids')
    elif decision == "2":
        video.streams.get_by_resolution("360p").download('/home/emre/avcioglu_vids')
    elif decision == "3":
        video.streams.get_by_resolution("480p").download('/home/emre/avcioglu_vids')
    elif decision == "4":
        video.streams.get_by_resolution("720p").download('/home/emre/avcioglu_vids')
    else:
        print("invalid input!")
        break

    print("\n\n")