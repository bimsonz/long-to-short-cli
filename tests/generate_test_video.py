import unittest
import os
from moviepy.editor import TextClip, concatenate_videoclips

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