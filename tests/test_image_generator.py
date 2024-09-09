import os

from pathlib import Path

from unittest import TestCase, mock

from src.midcli.lib import image_generator


class TestImageGenerator(TestCase):
    def setUp(self):
        for i in range(1, 3):
            Path(f'image{i}.png').touch(exist_ok=True)


    def tearDown(self):
        for path in Path().glob('*.png'):
            path.unlink()



    @mock.patch('src.midcli.lib.Client')
    def test_generation_image_png(self, mock_client: mock.MagicMock):
        mock_predict = mock_client().predict
        mock_predict.return_value = ([{'image': 'image1.png'}, {'image': 'image2.png'}], 0)

        image_generator('prompt_testing', 'style_test', 'my_image')

        [_, dict_call] = mock_predict.call_args

        self.assertEqual(dict_call['prompt'], 'prompt_testing')
        self.assertEqual(dict_call['style'], 'style_test')

        self.assertTrue(os.path.exists('my_image1.png'))
        self.assertTrue(os.path.exists('my_image2.png'))
