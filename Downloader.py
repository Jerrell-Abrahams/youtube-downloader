from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time

class Downloader:

    def __init__(self, link) -> None:
        self.videoSize = None
        self.size = None
        self.link = link
        self.percentage = 0


        try:
            self.yt = YouTube(self.link, on_progress_callback=self.progress_function)
            print("Found video -> " + self.yt.title)
            

        except (Exception):
            self.yt = None



    def percent(self, remaining, total):
        perc = round((1-remaining/total) * 100)
        return perc



    def progress_function(self, chuck, stream, bytes_remaining):
        self.size = self.videoSize.filesize
        percentage = self.percent(bytes_remaining, self.size)
        self.percentage = percentage
        print(self.percentage)
        return self.percentage


    def download_video(self, location, resolution):
        self.videoSize = self.yt.streams.filter(res=str(resolution)).first()
        self.yt.streams.filter(res=str(resolution)).first().download(output_path=location)

    def get_highest_resolution(self):
        return self.yt.streams.get_highest_resolution().resolution
    
    def get_title(self):
        return str(self.yt.title)

    def set_resolution(self, resolution):
        self.resolution = resolution
        return str(self.resolution)

    def download_audio_only(self, location):
        self.videoSize = self.yt.streams.filter(res="360p").first()
        self.yt.streams.filter(res="360p").first().download(output_path=location, filename=str(self.get_title()) + ".mp4")
        videoLocation = location + "/" + str(self.get_title()) + ".mp4"
        audioLocation = location + "/" + str(self.get_title()) + ".mp3"
        video = VideoFileClip(videoLocation)
        audio = video.audio
        audio.write_audiofile(audioLocation, verbose=False, logger=None)
        video.close()
        audio.close()
        os.remove(videoLocation)
        return


        