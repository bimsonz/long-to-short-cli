import unittest
import os
from moviepy.editor import VideoFileClip, ColorClip, concatenate_videoclips
from long_to_short_cli import process_video

def generate_test_video(output_file):
    clip1 = ColorClip(size=(1280, 720), color=(255, 0, 0)).set_duration(3)
    clip2 = ColorClip(size=(1280, 720), color=(0, 255, 0)).set_duration(3)
    clip3 = ColorClip(size=(1280, 720), color=(0, 0, 255)).set_duration(3)

    final_clip = concatenate_videoclips([clip1, clip2, clip3])
    final_clip.write_videofile(output_file, fps=24)

class TestLongToShortCLI(unittest.TestCase):
    def setUp(self):
        self.input_file = 'tests/input/video.mp4'
        self.output_file = 'tests/output/video.mp4'
        self.start_time = 2
        self.end_time = 7

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
        self.assertAlmostEqual(output_clip.duration, self.end_time - self.start_time, delta=0.1, msg="Output clip duration is incorrect")
        self.assertAlmostEqual(output_clip.aspect_ratio, 9 / 16, delta=0.01, msg="Output clip aspect ratio is incorrect")

if __name__ == '__main__':
    unittest.main()

