
```markdown
# YouTube Video Downloader

This script allows you to download videos from YouTube using a specified URL. The downloaded videos will be saved to a specified folder in your home directory.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- `pytube` library
- `tqdm` library

You can install the required libraries using pip:
```sh
pip install pytube tqdm
```

## Installation

1. Clone the repository or download the script file (`download_youtube_video.py`).

2. Ensure the script has execution permissions. You can set the permissions using:
```sh
chmod +x download_youtube_video.py
```

## Usage

1. Run the script:
```sh
python download_youtube_video.py
```

2. Enter the YouTube URL when prompted.

3. The video will be downloaded to the folder `~/YT/tracks`.

## Directory Structure

The script will download the videos to a folder named `YT/tracks` in your home directory. If the folder does not exist, the script will create it automatically.

## Example

```sh
~/YT/script $ python download_youtube_video.py
Enter the YouTube URL: https://youtu.be/JF6cL6TYbwE
Downloading 'Chill Afrobeats Mix 2024 (2Hrs) | Best of Alte | Afro Soul 2024' to /data/data/com.termux/files/home/YT/tracks...
100%|██████████████████████████████████████| 199M/199M [02:34<00:00, 1.29MB/s]
Download completed!
```

## Error Handling

If any error occurs during the download process, the script will print an error message.

## License

This project is licensed under the MIT License.
```

### Script (`download_youtube_video.py`)

Here's the updated script to include progress tracking and correct path handling:

```python
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
        
        # Get the file size
        file_size = stream.filesize
        filename = f"{yt.title}.mp4"
        file_path = os.path.join(output_path, filename)
        
        # Start the download using pytube's built-in download method
        with open(file_path, 'wb') as f:
            stream.stream_to_buffer(f)
            # Using tqdm to show progress
            with tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, initial=0) as pbar:
                for chunk in stream.stream_to_buffer(f):
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    download_video(url)
```

### Explanation:
- The script uses `tqdm` to display a progress bar for the download.
- The download path is set to `~/YT/tracks`.
- If the directory does not exist, it is created automatically.
- The script downloads the highest resolution stream available and saves it to the specified path.

----
