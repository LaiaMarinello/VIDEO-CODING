import os
import subprocess
from moviepy.editor import VideoFileClip

class Semi2:
    # EXERCISE 1:
    def generate_macroblocks_video(input_path, output_path):
        # Run FFMpeg command to generate video with macroblocks and motion vectors
        base_name, ext = os.path.splitext(os.path.basename(input_path))
        command = f"ffmpeg -hide_banner -flags2 +export_mvs -i {input_path} -vf codecview=mv=pf+bf+bb -an {output_path}"
        subprocess.run(command, shell=True, check=True)

    # EXERCISE 2:
    def create_new_bbb_container(input_path, output_cut, output_mono, output_stereo, output_aac, output_final):

        #Cut BBB into 50 seconds only video.
        os.system(f'ffmpeg -i {input_path} -t 50 -c:v copy -c:a copy {output_cut}')

        #Export BBB(50s) audio as MP3 mono track.
        os.system(f'ffmpeg -i {output_cut} -vn -ac 1 -ab 128k {output_mono}')

        #Export BBB(50s) audio in MP3 stereo w/ lower bitrate
        os.system(f'ffmpeg -i {output_cut} -vn -q:a 5 {output_stereo}')

        #Export BBB(50s) audio in AAC codec
        os.system(f'ffmpeg -i {output_cut} -vn -c:a aac {output_aac}')

        #Packaging everything in a .mp4:
        os.system(f'ffmpeg -i {output_cut} -i {output_mono} -i {output_stereo} -i {output_aac} -c:v copy -c:a copy {output_final}')

    # EXERCISE 3:
    def get_track_count(input_path):
        clip = VideoFileClip(input_path)
        track_count = len(clip.audio.tracks) + len(clip.video.tracks)
        return track_count


if __name__ == "__main__":

    # EXERCISE 2:
    input_path = "BigBuckBunny.mp4"
    output_cut = "BBB_50s.mp4"
    output_mono = "BBB_50s_mono.mp3"
    output_stereo = "BBB_50s_stereo.mp3"
    output_aac = "BBB_aac.aac"
    output_final = "BBB_final.mp4"
    Semi2.create_new_bbb_container(input_path, output_cut, output_mono, output_stereo, output_aac, output_final)

    # # EXERCISE 3:
    # track_count = Semi2.get_track_count(input_path)
    # print(f"The video '{input_path}' contains {track_count} tracks.")

    #EXERCISE 5:
    from Subtitles import Subtitles
    video_processor = Subtitles(
        '/home/laiamarinello/Documents/Semi2_Codification/BigBuckBunny.mp4',
        '/home/laiamarinello/Documents/Semi2_Codification/TheSmashingPumpkins.srt'
    )
    video_processor.integrate_subtitles('/home/laiamarinello/Documents/Semi2_Codification/BigBuckBunny_Subtitled.mp4')

    #EXERCISE 6:
    from YuvHistogram import YuvHistogram 
    input_video_path = "BigBuckBunny.mp4"
    output_video_path = "/home/laiamarinello/Documents/Semi2_Codification/BBBB_Histogram.mp4"

    yuv_histogram_processor = YuvHistogram(input_video_path, output_video_path)
    yuv_histogram_processor.integrate_yuv_histogram()