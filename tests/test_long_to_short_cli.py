import unittest
from unittest.mock import patch
import os
from moviepy.editor import VideoFileClip, ColorClip, concatenate_videoclips
from long_to_short_cli import process_video, time_str_to_seconds, crop_to_aspect_ratio, main

def generate_test_video(output_file, size=(1280, 720), aspect_ratio=(9, 16)):
    width, height = size
    clip1 = ColorClip(size=(width, height), color=(255, 0, 0)).set_duration(3)
    clip2 = ColorClip(size=(width, height), color=(0, 255, 0)).set_duration(3)
    clip3 = ColorClip(size=(width, height), color=(0, 0, 255)).set_duration(3)

    final_clip = concatenate_videoclips([clip1, clip2, clip3])

    if aspect_ratio:
        final_clip = crop_to_aspect_ratio(final_clip, aspect_ratio[0] / aspect_ratio[1])

    final_clip.write_videofile(output_file, fps=24)

class TestLongToShortCLI(unittest.TestCase):
    def setUp(self):
        self.input_file = 'tests/input/video.mp4'
        self.output_file = 'tests/output/video.mp4'
        self.start_time = '00:00:02'
        self.end_time = '00:00:07'

        input_dir = os.path.dirname(self.input_file)
        output_dir = os.path.dirname(self.output_file)

        if not os.path.exists(input_dir):
            os.makedirs(input_dir)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        generate_test_video(self.input_file)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_process_video(self):
        process_video(self.input_file, self.output_file, self.start_time, self.end_time)
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")

        output_clip = VideoFileClip(self.output_file)
        expected_duration = time_str_to_seconds(self.end_time) - time_str_to_seconds(self.start_time)
        self.assertAlmostEqual(output_clip.duration, expected_duration, delta=0.1, msg="Output clip duration is incorrect")
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

    def test_crop_to_aspect_ratio_landscape_input(self):
        landscape_input_file = 'tests/input/landscape_video.mp4'
        landscape_output_file = 'tests/output/landscape_video.mp4'

        generate_test_video(landscape_input_file, size=(1280, 720))

        process_video(landscape_input_file, landscape_output_file, self.start_time, self.end_time)

        self.assertTrue(os.path.exists(landscape_output_file), "Output file not created")

        output_clip = VideoFileClip(landscape_output_file)
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

        os.remove(landscape_input_file)
        os.remove(landscape_output_file)

    def test_crop_to_aspect_ratio_greater_than_9_16(self):
        input_file = 'tests/input/greater_than_9_16_video.mp4'
        output_file = 'tests/output/greater_than_9_16_video.mp4'

        generate_test_video(input_file, size=(500, 720))

        process_video(input_file, output_file, self.start_time, self.end_time)

        self.assertTrue(os.path.exists(output_file), "Output file not created")

        output_clip = VideoFileClip(output_file)
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

        os.remove(input_file)
        os.remove(output_file)

    def test_crop_to_aspect_ratio_equal_to_9_16(self):
        input_file = 'tests/input/equal_to_9_16_video.mp4'
        output_file = 'tests/output/equal_to_9_16_video.mp4'

        generate_test_video(input_file, size=(720, 1280))

        process_video(input_file, output_file, self.start_time, self.end_time)

        self.assertTrue(os.path.exists(output_file), "Output file not created")

        output_clip = VideoFileClip(output_file)
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

        os.remove(input_file)
        os.remove(output_file)

    def test_process_video_wider_aspect_ratio(self):
        # Use a video with a 16:9 aspect ratio
        generate_test_video(self.input_file, aspect_ratio=(16, 9))
        process_video(self.input_file, self.output_file, self.start_time, self.end_time)

        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        output_clip = VideoFileClip(self.output_file)
        self.assertAlmostEqual(output_clip.duration, 5, delta=0.1, msg="Output clip duration is incorrect")
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

    def test_invalid_start_time(self):
        with self.assertRaises(ValueError):
            process_video(self.input_file, self.output_file, "invalid_time", self.end_time)

    def test_invalid_end_time(self):
        with self.assertRaises(ValueError):
            process_video(self.input_file, self.output_file, self.start_time, "invalid_time")

    def test_main(self):
        with patch("sys.argv", ["long_to_short_cli.py", self.input_file, self.output_file, self.start_time, self.end_time]):
            main()

        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        output_clip = VideoFileClip(self.output_file)
        self.assertAlmostEqual(output_clip.duration, 5, delta=0.1, msg="Output clip duration is incorrect")
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

if __name__ == '__main__':
    unittest.main()
