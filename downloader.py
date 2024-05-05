# This code doesn't work.

from pytube import YouTube
from pytube import Channel
import os, string, re

c = Channel('https://www.youtube.com/channel/UCszy2T-XzqrpJ53qXWuzerw/videos')

print(c.channel_name)

downloadable_video_arr = []
local_video_arr = []


###
# Trimming the array strings for comparison without problem.
###

# Getting rid off the unnecessary characters
i = 0
for local_title in local_video_arr:
    print(i)
    local_video_arr[i] = re.sub(r'[^a-zA-Z0-9]', '', local_title)
    i = i+1

# Deleting last three letters, mp4.
i = 0
for local_title in local_video_arr:
    print(i)
    local_video_arr[i] = local_title[:-3]
    i = i+1

# Same process for downloadable array.
i = 0
for down_title in downloadable_video_arr:
    print(i)
    downloadable_video_arr[i] = re.sub(r'[^a-zA-Z0-9]', '', down_title)
    i = i+1


for title in downloadable_video_arr:
    print(title)

###
# Match founding algorithm, proceeds to deletes matching titles from the downloadable_video_arrey which already downloaded. 
###
# Create copies of the lists to avoid modifying them during iteration
downloadable_video_arr_copy = downloadable_video_arr[:]
local_video_arr_copy = local_video_arr[:]

for down_title in downloadable_video_arr_copy:
    for local_title in local_video_arr_copy:
        print("down_title = " + down_title)
        print("local_title = " + local_title + "\n\n\n")
        if down_title == local_title:
            print("Match found! Removing from the list which will be downloaded.")
            downloadable_video_arr.remove(local_title)
            break  # Break out of the inner loop once a match is found

for title in downloadable_video_arr:
    print("\n\nSonra")
    print(title)


# TODO: Find a way to remove the elemets from the list will be downloaded.

#for video in c.videos:
   # Only audio's will be downloaded.
#   print(video)
#   print(video.title + "\n")
#   video.streams.get_audio_only().download('/home/emre/avcioglu_vids')
#   print("\n\n")
