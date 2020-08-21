# Download YouTube Videos

This is a simple Python script I made with pafy, youtube-dl, ffpmeg, and moviepy. You can use it to download YouTube videos and cut them if you'd like. I created this because sometimes I like to edit videos, and I find it difficult to find a safe website to use to download YouTube videos.

## How To Use

DownloadYouTubeVid.py can be ran from the terminal using Python 3. First run pip install to download all the requirements

```bash
pip install requirements.txt
```

After doing so, you may run the python script on the terminal. It will first ask you to enter a YouTube link for the video you want to download. Just copy and paste the video link in the address bar.

```bash
Enter YouTube link of video to download: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

You may then decide whether you want to cut the video or not. If you would like to please input the "y" character in any case.

```bash
Would you like to cut the video (y/n)?: y
```

After you will be asked to input the start time and end time of the segment you'd like to cut out. Please follow the format HH:MM:SS to find the correct timestamp

```bash
Input the start time (HH:MM:SS): 00:01:30
Input the start time (HH:MM:SS): 00:03:00
```

Enjoy downloading and cutting videos!

