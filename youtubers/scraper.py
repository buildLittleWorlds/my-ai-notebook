import sys
import re
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

def get_video_data(video_url, file_name):
    """
    Fetches metadata and the transcript for a YouTube video and saves it to a text file.

    Args:
        video_url (str): The full URL of the YouTube video.
        file_name (str): The name for the output .txt file.
    """
    try:
        # Extract video ID from URL
        print("🔎 Fetching video data...")
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', video_url)
        if not video_id_match:
            raise ValueError("Invalid YouTube URL format")
        
        video_id = video_id_match.group(1)

        # Use yt-dlp to get video information
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
        # --- 1. Get Video Information ---
        video_title = info.get('title', 'Unknown Title')
        channel_title = info.get('uploader', 'Unknown Channel')
        # Format date as "Month Day, Year"
        upload_date = info.get('upload_date', '')
        if upload_date:
            from datetime import datetime
            date_obj = datetime.strptime(upload_date, '%Y%m%d')
            publish_date = date_obj.strftime("%B %d, %Y")
        else:
            publish_date = "Unknown Date"

        # --- 2. Get Video Transcript ---
        print("📖 Getting transcript...")
        try:
            # Fetch the transcript using the video ID
            transcript_api = YouTubeTranscriptApi()
            transcript = transcript_api.fetch(video_id)
            
            # Join the 'text' parts of the transcript into a single string
            transcript_text = " ".join([snippet.text for snippet in transcript.snippets])
            
        except (NoTranscriptFound, TranscriptsDisabled) as e:
            # Handle cases where transcripts are not available
            transcript_text = "Transcript is not available for this video."
        except Exception as e:
            # Handle any other transcript-related errors
            transcript_text = f"Error fetching transcript: {str(e)}"

        # --- 3. Write all information to a .txt file ---
        # Ensure the filename ends with .txt
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        
        # Create the full path to save in transcripts directory
        import os
        output_path = os.path.join('transcripts', file_name)

        print(f"✍️ Writing information to '{output_path}'...")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"URL: {video_url}\n")
            f.write("="*30 + "\n") # Separator
            f.write(f"Channel Title: {channel_title}\n")
            f.write(f"Video Title: {video_title}\n")
            f.write(f"Publish Date: {publish_date}\n")
            f.write("="*30 + "\n\n")
            f.write("TRANSCRIPT:\n\n")
            f.write(transcript_text)

        print(f"\n✅ Success! Information saved to '{output_path}'")

    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("Please use a standard YouTube video URL (e.g., 'https://www.youtube.com/watch?v=...')")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please check the URL and your internet connection.")

# --- Main part of the script that runs when executed ---
if __name__ == "__main__":
    print("YouTube Video Info & Transcript Downloader 🎬")
    
    # Check if command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python scraper.py <youtube_url> <output_filename>")
        print("Example: python scraper.py 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' 'video_data'")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2]
    
    # Call the function with the command line arguments
    get_video_data(url, filename)