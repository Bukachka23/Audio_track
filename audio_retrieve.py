
import moviepy.editor
from pathlib import Path

# video_file.stem - Fixes the file name, but ignores the file extension
video_file = Path("имя_файла")                          # video file path

# указываем модуль файлу с которым он бдует работать
video = moviepy.editor.VideoFileClip(f"{video_file}")   # Turning to the video clip class
audio = video.audio                                     # Retrieve the audio tracks of the file by accessing "audio"
audio.write_audiofile(f"{video_file.stem}.mp3")         # Saving audio to a file