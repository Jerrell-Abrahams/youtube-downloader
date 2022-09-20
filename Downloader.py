from pytube import YouTube

class Downloader:
    link = ""
    resolution = ""

    def __init__(self, link) -> None:
        self.link = link
        try:
            yt = YouTube(self.link)
            
        except (Exception):
            print("Could not get video")

    def download_video(self):
        yt.streams.filter(res="720p").first().download()

    def get_highest_resolution(self):
        pass

    def get_title(self):
        pass

    def set_resolution(self, resolution):
        self.resolution = resolution
        return str(self.resolution)

    def download_audio_only(self):
        pass

download = Downloader("https://www.youtube.com/watch?v=8ggtEzQ63oY&ab_channel=TristynLee")

download.download_video()