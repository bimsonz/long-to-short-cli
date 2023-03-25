# long-to-short-cli Video Cropper

`long-to-short-cli` is a user-friendly command-line tool that allows you to crop a video to a 9:16 aspect ratio and extract a specific portion based on start and end times. This tool is built using the powerful MoviePy library for video editing in Python. It's perfect for creating social media clips or quickly trimming videos while maintaining high-quality audio and video.

## Requirements
- Python 3.6 or higher
- MoviePy

## Installation
1. Clone or download the repository:

`git clone https://github.com/bimsonz/long-to-short-cli.git`


2. Navigate to the project directory:

`cd long-to-short-cli`


3. Install the required dependencies:

`pip3 install -r requirements.txt`


## Usage

1. Run the `long_to_short_cli.py` script with the following command:

`python3 long_to_short_cli.py path/to/your/video.mp4 path/to/output/video.mp4 start_time end_time`


Replace `path/to/your/video.mp4` with the path to the input video file, `path/to/output/video.mp4` with the path to the output video file, `start_time` with the start time of the clip (in seconds), and `end_time` with the end time of the clip (in seconds).

Example:

`python long_to_short_cli.py input_video.mp4 output_video.mp4 10 40`


This command will create a cropped video with a 9:16 aspect ratio, extracting the portion between 10 and 40 seconds from the input video.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
