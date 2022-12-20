# importing packages
from pytube import Playlist
import os
import json

###
# Before running program enter the following information
# Hold option on folder of storage and click copy as directory
# Or put dot to save to this directory
dirToStorage = '.'

# Also create an playlists.json file with the playlists you want to download
# (file with example included)
###

with open('playlists.json', 'r') as file:
    playlists = json.load(file)['playlists']

for playlist in playlists:
    print(f'Downloading {playlist["name"]}')
    # get the playlist link and put it in an object
    p = Playlist(playlist['link'])

    playlistLength = p.length
    downloadedNum = 0

    # create a file for the album to go in
    storage = dirToStorage + '/' + playlist['name']
    os.mkdir(storage)

    print(f'{str(downloadedNum).zfill(len(str(playlistLength)))} / {str(playlistLength).zfill(len(str(playlistLength)))}', flush=True, end='')
    print('\b' * (((len(str(playlistLength)) * 2) + 1)), flush=True, end='')

    for video in p.videos:
        # get the song and filter only the audio ***(change to false to get video)***
        songFile = song.streams.filter(only_audio=True).first()
        # download the song
        finalFile = songFile.download(output_path=storage)
        # splits the song into the base (file name) and extenstion (eg file.txt file is base .txt is ext)
        base, ext = os.path.splitext(finalFile)
        # makes the new file name the base but changes the extension to .mp3 ***(if downloading video, change .mp3 to .mp4)***
        newFile = base + '.mp3'
        # renames the file
        os.rename(finalFile, newFile)

        downloadedNum += 1
        if(downloadedNum < 10):
            print('\b', flush=True, end='')
        else:
            print('\b\b', flush=True, end='')
        
        print(downloadedNum, flush=True, end='')
        

    print('')