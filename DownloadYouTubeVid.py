import pafy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

link = input("Enter YouTube link of video to download: ")
v = pafy.new(link)
s = v.getbest()
print("Size is %s" % s.get_filesize())
filename = s.download()  # starts download

choice = input("Would you like to cut the video (y/n)?: ")

if choice.upper() == "Y":
    # Ask for time stamps
    start_t = input("Input the start time (HH:MM:SS): ") 
    end_t = input("Input the end time (HH:MM:SS): ")

    # Converts time into seconds
    start_time = (int(start_t[:2]) * 3600) + (int(start_t[3:5]) * 60) + (int(start_t[6:8])) 
    end_time = (int(end_t[:2]) * 3600) + (int(end_t[3:5]) * 60) + (int(end_t[6:8])) 

    ffmpeg_extract_subclip(f"{s.title}.mp4", start_time, end_time, targetname=f"{s.title}_cut.mp4") # cuts the clip
