# Long to Short CLI
[![PyPI version](https://badge.fury.io/py/long-to-short-cli.svg)](https://badge.fury.io/py/long-to-short-cli)
![PyPI - Downloads](https://img.shields.io/pypi/dm/long-to-short-cli)
[![Run Tests](https://github.com/bimsonz/long-to-short-cli/actions/workflows/test.yml/badge.svg)](https://github.com/bimsonz/long-to-short-cli/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/bimsonz/long-to-short-cli/badge.svg?branch=main&bust=1)](https://coveralls.io/github/bimsonz/long-to-short-cli?branch=main)

A command-line tool for cropping and trimming video files. Easily extract a desired portion of a video and convert it to a vertical video (9:16 aspect ratio). This tool uses the [MoviePy](https://zulko.github.io/moviepy/) library to process videos. It's perfect for creating social media clips or quickly trimming videos while maintaining high-quality audio and video.

## Installation

### Prerequisites

- Python 3 (Refer to the [official Python documentation](https://www.python.org/downloads/) for installation instructions)
- FFmpeg (Refer to the [official FFmpeg documentation](https://ffmpeg.org/download.html) for installation instructions)

### Install the Package


You can install the package using `pip3`:

```bash
pip3 install long-to-short-cli
```


## Usage

To use the script, run the following command:

1. Run the `long-to-short-cli` script with the following command:

```
long-to-short-cli my_video.mp4 cropped_video.mp4 10 40
```

Replace `input_video.mp4` with the path to the input video file, `output_video.mp4` with the desired output file path, and `start_time` and `end_time` with the desired start and end times of the clip in `HH:MM:SS`, `MM:SS`, or `SS` format.

Example:

```
long-to-short-cli my_video.mp4 cropped_video.mp4 00:00:10 00:00:40
```

This command will extract a clip from `my_video.mp4` starting at 10 seconds (00:00:10) and ending at 40 seconds (00:00:40), convert it to a 9:16 aspect ratio, and save the result as `cropped_video.mp4`.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
