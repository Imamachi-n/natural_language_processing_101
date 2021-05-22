import unittest

from src.packages import deleteStopword


class TestDeleteStopword(unittest.TestCase):
    def test_delete_stopword(self):
        actual = deleteStopword.download_jp_stopwords()
        self.assertEqual(True, isinstance(actual, set))
