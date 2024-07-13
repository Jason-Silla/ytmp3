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

3) Install pytube

Go to the terminal on your computer and type "pip3 install pytube". This will install the latest version of pytube onto your computer.

---------------------

4) Fix pytube code

Type into the terminal "pip3 show pytube". Navigate to that directory on your computer. Open cipher.py file and go to line 264. Replace function_patterns array with this one:

        function_patterns = [
            # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
            # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
            # var Bpa = [iha];
            # ...
            # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
            # Bpa.length || iha("")) }};
            # In the above case, `iha` is the relevant function name
            r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
            r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
            r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
        ]

Save the file.

---------------------

5) Run the program by typing "python3 main.py" into the terminal while the terminal is in the directory of the file.
