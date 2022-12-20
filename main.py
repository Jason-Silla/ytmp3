# importing packages
from pytube import Playlist
import os
import json

###
# Before running program enter the following information
# Hold option on folder of storage and click copy as directory
# Or put dot to save to this directory
dirToStorage = '/Users/jasonsilla/Desktop/Music/Albums'

# Also create an albums.json file with the albums you want to download
# (file with example included)
###

with open('albums.json', 'r') as file:
    albums = json.load(file)['albums']

for album in albums:
    print(f'Downloading {album["name"]}')
    # get the album link and put it in an object
    p = Playlist(album['link'])

    albumLength = p.length
    downloadedNum = 0

    # create a file for the album to go in
    storage = dirToStorage + '/' + album['name']
    os.mkdir(storage)

    print(f'{str(downloadedNum).zfill(len(str(albumLength)))} / {str(albumLength).zfill(len(str(albumLength)))}', flush=True, end='')
    print('\b' * (((len(str(albumLength)) * 2) + 1)), flush=True, end='')

    for song in p.videos:
        # get the song and filter only the audio
        songFile = song.streams.filter(only_audio=True).first()
        # download the song
        finalFile = songFile.download(output_path=storage)
        # splits the song into the base (file name) and extenstion (eg file.txt file is base .txt is ext)
        base, ext = os.path.splitext(finalFile)
        # makes the new file name the base but changes the extension to .mp3
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