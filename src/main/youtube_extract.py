from pytube import YouTube
import os
import csv
import pandas as pd
import ffmpeg

links_meta = pd.read_csv('youtube_links.csv')

for i in links_meta:
    yt = YouTube(i)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    audio_input = ffmpeg.input(new_file)
    audio_cut = audio_input.audio.filter('atrim', duration=60)
    audio_output = ffmpeg.output(audio_cut, base+'_trim.mp3')
    ffmpeg.run(audio_output)