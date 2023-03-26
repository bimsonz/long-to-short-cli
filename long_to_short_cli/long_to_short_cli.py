import argparse
from moviepy.editor import VideoFileClip

def time_str_to_seconds(time_str):
    time_parts = list(map(int, time_str.split(':')))
    seconds = 0

    for part in time_parts:
        seconds = seconds * 60 + part

    return seconds

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

    start_time_seconds = time_str_to_seconds(start_time)
    end_time_seconds = time_str_to_seconds(end_time)

    selected_clip = video.subclip(start_time_seconds, end_time_seconds)

    aspect_ratio = 9 / 16
    cropped_video = crop_to_aspect_ratio(selected_clip, aspect_ratio)

    cropped_video = cropped_video.set_audio(selected_clip.audio)

    cropped_video.write_videofile(output_video, codec='libx264', bitrate='5000k', audio_codec='aac', audio_bitrate='320k', threads=4)

def main():
    parser = argparse.ArgumentParser(description='Extract a clip using start and end times and crop to 9:16 aspect ratio using MoviePy')
    parser.add_argument('input_video', type=str, help='Path to the input video file')
    parser.add_argument('output_video', type=str, help='Path to the output video file')
    parser.add_argument('start_time', type=str, help='Start time of the clip (in format HH:MM:SS, MM:SS, or SS)')
    parser.add_argument('end_time', type=str, help='End time of the clip (in format HH:MM:SS, MM:SS, or SS)')

    args = parser.parse_args()

    process_video(args.input_video, args.output_video, args.start_time, args.end_time)

if __name__ == '__main__':
    main()
