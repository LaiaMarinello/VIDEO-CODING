#Lab 2 - Video Coding - Created by Laia Marinel·lo
import subprocess
import json
import sys #EXERCISE 5!


# EXERCISE 1
input_video = "/home/laiamarinello/Documents/Lab2_Codification/BigBuckBunny.mp4"  # Input video file
output_video = "BigBuckBunny.mpg"  # Output video file (MP2 format)

# Conversion using the ffmpeg command
ffmpeg_convert_cmd = f'ffmpeg -i {input_video} -c:v mpeg2video {output_video}'
subprocess.call(ffmpeg_convert_cmd, shell=True)
print(f"Video converted to {output_video}")

# Parse video info using ffmpeg
ffmpeg_info_cmd = f'ffprobe -v error -show_entries stream=codec_name,width,height,duration,nb_frames,r_frame_rate -of json {input_video}' 
video_info = subprocess.check_output(ffmpeg_info_cmd, shell=True).decode('utf-8')
info_file = open('video_info.txt', 'w')
info_file.write(video_info)
info_file.close()
print("Video info saved to video_info.txt")


# EXERCISE 2
def modify_resolution(input_video, output_video, new_resolution):
    # FFmpeg command to change the resolution
    ffmpeg_cmd = f'ffmpeg -i {input_video} -vf "scale={new_resolution}" {output_video}'
    subprocess.call(ffmpeg_cmd, shell=True)

# Usage of the modify_resolution function
new_resolution = "1280x720"  # Change to the desired resolution
output_resized_video = "BigBuckBunny_resized.mpg"  # Output resized video file
modify_resolution(output_video, output_resized_video, new_resolution)
print(f"Video resolution modified and saved to {output_resized_video}")


# EXERCISE 3
def change_chroma_subsampling(input_video, output_video, subsampling_format="yuv420p"):
    # FFmpeg command to change chroma subsampling
    ffmpeg_cmd = f'ffmpeg -i {input_video} -pix_fmt {subsampling_format} {output_video}'
    subprocess.call(ffmpeg_cmd, shell=True)

# Usage of the change_chroma_subsampling function
new_subsampling = "yuv422p"  # Change to the desired subsampling format
output_with_changed_subsampling = "BigBuckBunny_changed_subsampling.mpg"  # Output video file
change_chroma_subsampling(output_resized_video, output_with_changed_subsampling, new_subsampling)
print(f"Chroma subsampling changed and saved to {output_with_changed_subsampling}")


# EXERCISE 4
def read_video_info(input_video):
    # FFmpeg command to read video info
    ffmpeg_info_cmd = f'ffprobe -v error -show_entries stream=codec_name,width,height,duration,nb_frames,r_frame_rate -of json {input_video}' 

    try:
        result = subprocess.run(ffmpeg_info_cmd, shell=True, capture_output=True, text=True, check=True)
        output = result.stdout

        # Parse the JSON output
        data = json.loads(output)
        video_stream = data['streams'][0]

        # Print relevant data
        print(f"Codec Name: {video_stream['codec_name']}")
        print(f"Resolution: {video_stream['width']}x{video_stream['height']}")
        print(f"Duration: {video_stream['duration']} seconds")
        print(f"Frame Rate: {video_stream['r_frame_rate']}")
        print(f"Number of Frames: {video_stream['nb_frames']}")

    except subprocess.CalledProcessError as e:
        print(f"Error running FFmpeg: {e}")

# Usage of the read_video_info function
input_video = "BigBuckBunny.mp4"  # Change to the input video file
read_video_info(input_video)


#EXERCISE 5
sys.path.append("/home/laiamarinello/Documents/Lab1_Codification")
import Lab1

R = float(input("R (0 to 255): "))
G = float(input("G (0 to 255): "))
B = float(input("B (0 to 255): "))
Y, U, V = Lab1.rgb_to_yuv(R, G, B)
print('Y is:', Y)
print('U is:', U)
print('V is:', V)