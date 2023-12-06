import subprocess
import os

#EXERCISE 6 - Yuv Histogram:
class YuvHistogram:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def integrate_yuv_histogram(self):
        input_name, ext = os.path.splitext(os.path.basename(self.input_path))

        # Create default output_path if not provided
        if not self.output_path:
            self.output_path = f"{input_name}_histogram{ext}"

        cmd = (
            f'ffmpeg -hide_banner -i {self.input_path} -vf "split=2[a][b],[b]histogram,'
            f'format=yuva444p[hh],[a][hh]overlay" {self.output_path}'
        )
        subprocess.run(cmd, shell=True, check=True)

        print(f"YUV Histogram integrated successfully into {self.output_path}")

