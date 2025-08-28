import unittest

from get_response import emotion_detector, format_output

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(format_output(emotion_detector("I am glad this happened"))["dominant_emotion"], "joy")
    
    def test_anger(self):
        self.assertEqual(format_output(emotion_detector("I am really mad about this	"))["dominant_emotion"], "anger")

    def test_disgust(self):
        self.assertEqual(format_output(emotion_detector("I feel disgusted just hearing about this"))["dominant_emotion"], "disgust")

    def test_sad(self):
        self.assertEqual(format_output(emotion_detector("I am so sad about this"))["dominant_emotion"], "sadness")

    def test_fear(self):
        self.assertEqual(format_output(emotion_detector("I am really afraid that this will happen"))["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()