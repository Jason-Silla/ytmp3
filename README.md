# ytmp3
A python program that converts YouTube playlists to mp3 files.

# Steps:
1) Add the directory that you want the playlist saved to as an absolute path.

Save this to the variable dirToStorage. By default, it will save the downloads to the directory that you have the file in.

-------------------

2) Add all of the playlists you would like to download into the json file included.


        {
          "playlists": [
            {
              "name": "[name of playlist]",
              "link": "[link to playlist on YouTube]"
            },
            {
              "name": "[name of playlist]",
              "link": "[name of playlist]"
            }
          ]
        }

MAKE SURE THAT THE SYNTAX IS PERFECT OR ELSE IT WILL NOT WORK
-

If you want to add more playlists to the download file, copy and paste the code below and put it DIRECTLY below the previous playlist section.

        {
          "name": "[name of playlist]",
          "link": "[link to playlist on YouTube]"
        }

Make sure to add a comma at the end of the previous section like in the example.

---------------------

3) Run the program by typing "python3 main.py" into the terminal while the terminal is in the directory of the file.
