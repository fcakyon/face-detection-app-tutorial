import unittest
from io import BytesIO

class TestApiEndpoints(unittest.TestCase):
    def test_detect_with_3ch(self):
        from app import app

        client = app.test_client()

        # test image
        image_path = "tests/data/sample1.jpg"
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        response = client.post(
            "/detect", data = {'image': (BytesIO(image_bytes), 'sample1.jpg')}, content_type='multipart/form-data',
        )

        self.assertEqual(len(response.json["detections"]), 4)

    def test_detect_with_4ch(self):
        from app import app

        client = app.test_client()

        # test image
        image_path = "tests/data/sample0.png"
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        response = client.post(
            "/detect", data = {'image': (BytesIO(image_bytes), 'sample0.png')}, content_type='multipart/form-data',
        )

        self.assertEqual(len(response.json["detections"]), 4)