from pytube import YouTube
from pytube import Channel
import os, string, re

c = Channel('https://www.youtube.com/channel/UCszy2T-XzqrpJ53qXWuzerw/videos')

print(c.channel_name)

downloadable_video_arr = []
local_video_arr = []

for video in c.videos:
   # Only audio's will be downloaded.
   print(video.title + "\n")
   video.streams.get_audio_only().download('/home/emre/avcioglu_vids')
   print("\n\n")