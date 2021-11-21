from pytube import YouTube
from playsound import playsound
from os import path
from os import system

def essela(a, b):
    system("gnome-terminal -- python3 " + path.basename(__file__))
    system("gnome-terminal -- python3 " + path.basename(__file__))
    system("amixer -D pulse sset Master 100%")
    system("amixer -D pulse sset Master unmute")
    playsound(path.expanduser('~/Music/sela.mp3'))

if not path.exists(path.expanduser('~/Music/sela.mp3')):
    yt = YouTube('https://www.youtube.com/watch?v=7unENFLHAVs', on_complete_callback = essela)
    yt.streams.filter(only_audio=True).desc().first().download(output_path=path.expanduser('~/Music'), filename=".sela.mp3")
else:
    essela(0, 0)
