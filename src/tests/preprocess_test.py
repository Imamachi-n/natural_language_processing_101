import unittest

from src.packages import cleanText


class TestCleanText(unittest.TestCase):

    def test_clean_text(self):
        actual = cleanText.clean_text(" てすと\r\nテスト　")
        self.assertEqual("てすと\nテスト", actual)
