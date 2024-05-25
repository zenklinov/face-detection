import unittest
import cv2
from src.face_detection import detect_faces

class TestFaceDetection(unittest.TestCase):
    def test_detect_faces(self):
        frame = cv2.imread('path_to_test_image.jpg')
        result_frame = detect_faces(frame)
        self.assertIsNotNone(result_frame)

if __name__ == '__main__':
    unittest.main()
