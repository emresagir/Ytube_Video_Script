from pytube import YouTube
from pytube import Channel

c = Channel('https://www.youtube.com/channel/UCszy2T-XzqrpJ53qXWuzerw/videos')

print(c.channel_name)

for video in c.videos:
    # Only audio's will be downloaded.
    print(video.title + "\n")
    print(video.streams.filter(only_audio=True))
    print("\n\n")



