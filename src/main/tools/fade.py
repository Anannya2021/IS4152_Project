import os
import pydub
from pydub import AudioSegment

for filename in os.listdir('./Happy'):
    if filename.endswith(".mp3"):
        song = AudioSegment.from_mp3('./Happy/'+filename)
        faded_song = song.fade_in(1000).fade_out(3000)
        faded_song.export('./Happy_fade/'+filename, format="mp3")
