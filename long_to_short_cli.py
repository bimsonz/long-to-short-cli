import argparse
from moviepy.editor import VideoFileClip

def crop_to_aspect_ratio(clip, aspect_ratio):
    width, height = clip.size
    new_width = int(height * aspect_ratio)

    if new_width > width:
        new_height = int(width / aspect_ratio)
        crop_y = (height - new_height) // 2
        return clip.crop(y1=crop_y, y2=crop_y + new_height)
    else:
        crop_x = (width - new_width) // 2
        return clip.crop(x1=crop_x, x2=crop_x + new_width)

def process_video(input_video, output_video, start_time, end_time):
    video = VideoFileClip(input_video)

    selected_clip = video.subclip(start_time, end_time)

    aspect_ratio = 9 / 16
    cropped_video = crop_to_aspect_ratio(selected_clip, aspect_ratio)

    # Preserve the audio from the original video
    cropped_video = cropped_video.set_audio(selected_clip.audio)

    # Write the output video file with specified codecs, bitrates, and threads
    cropped_video.write_videofile(output_video, codec='libx264', bitrate='5000k', audio_codec='aac', audio_bitrate='320k', threads=4)

def main():
    parser = argparse.ArgumentParser(description='Extract a clip using start and end times and crop to 9:16 aspect ratio using MoviePy')
    parser.add_argument('input_video', type=str, help='Path to the input video file')
    parser.add_argument('output_video', type=str, help='Path to the output video file')
    parser.add_argument('start_time', type=float, help='Start time of the clip (in seconds)')
    parser.add_argument('end_time', type=float, help='End time of the clip (in seconds)')

    args = parser.parse_args()

    process_video(args.input_video, args.output_video, args.start_time, args.end_time)

if __name__ == '__main__':
    main()
