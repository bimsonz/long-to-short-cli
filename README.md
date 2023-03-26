# Long to Short CLI
[![Run Tests](https://github.com/bimsonz/long-to-short-cli/actions/workflows/test.yml/badge.svg)](https://github.com/bimsonz/long-to-short-cli/actions/workflows/test.yml)

A command-line tool for cropping and trimming video files. Easily extract a desired portion of a video and convert it to a vertical video (9:16 aspect ratio). This tool uses the [MoviePy](https://zulko.github.io/moviepy/) library to process videos. It's perfect for creating social media clips or quickly trimming videos while maintaining high-quality audio and video.

## Requirements

- Python 3.6 or higher

## Installation

1. Make sure you have Python 3.6 or higher installed on your system. If you don't have it installed, you can download it from the [official Python website](https://www.python.org/downloads/).

2. Go to the "Releases" tab in the [long-to-short-cli GitHub repository](https://github.com/bimsonz/long-to-short-cli/releases) and download the latest release source code as a ZIP or TAR.GZ archive.

3. Extract the downloaded archive to a directory of your choice.

4. Open a terminal or command prompt and navigate to the extracted directory:

5. Navigate to the project directory:

`cd long-to-short-cli`

6. Install the required dependencies:

`pip3 install -r requirements.txt`



## Usage

To use the script, run the following command:

1. Run the `long_to_short_cli.py` script with the following command:

`python3 long_to_short_cli.py my_video.mp4 cropped_video.mp4 10 40`

Replace `input_video.mp4` with the path to the input video file, `output_video.mp4` with the desired output file path, and `start_time` and `end_time` with the desired start and end times of the clip in `HH:MM:SS`, `MM:SS`, or `SS` format.

Example:

`python3 long_to_short_cli.py my_video.mp4 cropped_video.mp4 00:00:10 00:00:40`

This command will extract a clip from `my_video.mp4` starting at 10 seconds (00:00:10) and ending at 40 seconds (00:00:40), convert it to a 9:16 aspect ratio, and save the result as `cropped_video.mp4`.


## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
