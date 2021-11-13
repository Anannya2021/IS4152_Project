# Investigating Affective States with Music - IS4152/5152 Project

This project was done as a part of IS4152/IS5152 module. With this project we aim to find the effect music has on an individual's affective states. 

## Table of Contents
1. Dataset Generation
2. Classification Models
3. Statistical Inference

## 1. Dataset Generation

To create the dataset, songs can be sourced from either Spotify music library or last.fm website. In this code base, there are two folders available under src/main/datasets. src/main/datasets/last.fm folder contains a python script for connecting to the last.fm API by providing a URL as a system argument. The songs returned by last.fm are searched for in Spotify library and the audio features for matching ones are collected.

Command to source songs and audio features based on last.fm playlists:

`
python last_fm_dataset.py "https://ws.audioscrobbler.com/2.0/?method=tag.gettopalbums&tag=Energetic&api_key=0d5cf010febef894eb16adda9a85b41e&format=json" energetic_songs.csv
`

Command to source songs and audio features from Spoitfy:

`
python dataset-create.py
`

## 2. Classification Model


