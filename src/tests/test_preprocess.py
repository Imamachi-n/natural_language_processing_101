import unittest

from src.packages import cleanText


class TestCleanText(unittest.TestCase):

    def test_clean_text(self):
        actual = cleanText.clean_text(" てすと\r\nテスト　")
        self.assertEqual("てすと\nテスト", actual)


if __name__ == "__main__":
    unittest.main()
