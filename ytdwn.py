import os
from pytube import YouTube
from tqdm import tqdm

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_path = os.path.join(os.path.expanduser('~'), 'YT', 'tracks')  # Path to ~/YT/tracks
        if not os.path.exists(output_path):
            os.makedirs(output_path)  # Create the directory if it doesn't exist
        print(f"Downloading '{yt.title}' to {output_path}...")
        
        # Start the download using pytube's built-in download method
        stream.download(output_path=output_path, filename=f"{yt.title}.mp4", 
                        filename_prefix=None, skip_existing=False)
        
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    download_video(url)
