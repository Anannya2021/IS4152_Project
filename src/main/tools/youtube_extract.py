from pytube import YouTube
import os
import csv
import pandas as pd
import ffmpeg
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

links_meta = pd.read_csv('youtube_links.csv')

links_meta_list = links_meta['Links'].values.tolist()

for i in links_meta_list:
    yt = YouTube(i)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="raw_audio_files_sad")
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    ffmpeg_cmd = (
            ffmpeg
                .input(new_file, ss=0, t=60)
                .output(base+'_trim.mp3', acodec='mp3')
                .overwrite_output()
        )
    ffmpeg_cmd.run()
    
    
