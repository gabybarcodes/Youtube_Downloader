from pytube import YouTube

class YoutubeAudioDownloader:
    def __init__(self, video_url):
        self.video_url = video_url

    def download_audio(self, output_path= "downloads"):
        try:
            # Create a YouTube object
            yt = YouTube(self.video_url)

            # Get the best audio stream
            audio_stream = yt.streams.filter(only_audio= True).first()

            # Define the output file path
            output_file_path = f"{output_path}/{yt.title}.mp3"

            # Download the audio stream
            print(f"Downloading audio: {yt.title}")
            audio_stream.download(output_path=output_path, filename=yt.title + ".mp3")

            print(f"Audio downloaded successfully to: {output_file_path}")
        except Exception as e:
            print(f"Error: {e}")

video_url = "https://www.youtube.com/watch?v=U6gCkrzfsEU"
audio_downloader = YoutubeAudioDownloader(video_url)
audio_downloader.download_audio() 
