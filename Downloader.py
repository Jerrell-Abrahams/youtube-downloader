import time
from pytube import YouTube

class Downloader:

    def __init__(self, link) -> None:
        self.link = link
        

        # def progress_function(stream, chunk, bytes_remaining):
        #     size = stream.filesize
        #     progress += (float(abs(bytes_remaining-size)/size))*float(100)

        try:
            self.yt = YouTube(self.link)
            # self.yt.register_on_progress_callback(progress_function)

        except (Exception):
            self.yt = None

    def download_video(self, location, resolution):
        self.yt.streams.filter(res=str(resolution)).first().download(output_path=location)

    def get_highest_resolution(self):
        return self.yt.streams.get_highest_resolution().resolution
    
    def get_title(self):
        return str(self.yt.title)

    def set_resolution(self, resolution):
        self.resolution = resolution
        return str(self.resolution)

    def download_audio_only(self, location):
        self.yt.streams.filter(only_audio=True).first().download(output_path=location)
    

    def percent(self):
        while True:
            time.sleep(1)
            if self.progress == 100:
                break
            return self.progress