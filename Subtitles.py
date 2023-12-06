import subprocess
import chardet

#EXERCISE 4 - Subtitles
class Subtitles:
    def __init__(self, video_path, subtitles_path):
        self.video_path = video_path
        self.subtitles_path = subtitles_path

    def detect_encoding(self, file_path):
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
            return result['encoding']

    def integrate_subtitles(self, output_path):
        subtitles_encoding = self.detect_encoding(self.subtitles_path)
        command = (
            f'ffmpeg -i "{self.video_path}" -vf '
            f'"subtitles={self.subtitles_path}:charenc={subtitles_encoding}" "{output_path}"'
        )
        subprocess.run(command, shell=True, check=True)

