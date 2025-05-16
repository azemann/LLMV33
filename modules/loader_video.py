import subprocess
import tempfile
import os

def transcribe_video_audio(video_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_file:
        audio_path = audio_file.name
    subprocess.run(["ffmpeg", "-i", video_path, "-vn", "-acodec", "libmp3lame", audio_path])
    from .loader_audio import transcribe_audio
    return transcribe_audio(audio_path)
