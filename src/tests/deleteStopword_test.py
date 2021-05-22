import unittest

from src.packages import deleteStopword


class TestDeleteStopword(unittest.TestCase):
    def test_download_stopword(self):
        actual = deleteStopword.download_jp_stopwords()
        self.assertEqual(True, isinstance(actual, list))

    def test_delete_stopword(self):
        stopword_list = deleteStopword.download_jp_stopwords()
        actual = deleteStopword.delete_stopwords(
            ["りんご", "を", "いくつ", "か", "買う", "。"], stopword_list
        )
        self.assertEqual(["りんご", "を", "か", "買う", "。"], actual)
