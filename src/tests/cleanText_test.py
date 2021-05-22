import unittest

from src.packages import cleanText


class TestCleanText(unittest.TestCase):
    def test_clean_text_1(self):
        actual = cleanText.clean_text(" てすと\r\nテスト　")
        self.assertEqual("てすと\nテスト", actual)

        actual = cleanText.clean_text("【てすと】 テスト")
        self.assertEqual(" てすと  テスト", actual)

        actual = cleanText.clean_text("（てすと） テスト")
        self.assertEqual(" てすと  テスト", actual)

        actual = cleanText.clean_text("(てすと) テスト")
        self.assertEqual(" てすと  テスト", actual)

        actual = cleanText.clean_text("[てすと] テスト")
        self.assertEqual(" てすと  テスト", actual)

        actual = cleanText.clean_text("@てすと テスト")
        self.assertEqual(" テスト", actual)

        actual = cleanText.clean_text("＠てすと テスト")
        self.assertEqual(" テスト", actual)

        actual = cleanText.clean_text("てすと http://example.com test")
        self.assertEqual("てすと  test", actual)

        actual = cleanText.clean_text("てすと https://example.com test")
        self.assertEqual("てすと  test", actual)

        actual = cleanText.clean_text("てすと https://example.com")
        self.assertEqual("てすと ", actual)
