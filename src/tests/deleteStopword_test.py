import unittest

from src.packages import deleteStopword


class TestDeleteStopword(unittest.TestCase):
    def test_download_stopword(self):
        path = deleteStopword.download_jp_stopwords()
        actual = deleteStopword.get_stopwords(path)
        self.assertEqual(True, isinstance(actual, list))

    def test_delete_stopword(self):
        path = deleteStopword.download_jp_stopwords()
        stopword_list = deleteStopword.get_stopwords(path)
        actual = deleteStopword.delete_stopwords(
            ["りんご", "を", "いくつ", "か", "買う", "。"], stopword_list
        )
        self.assertEqual(["りんご", "を", "か", "買う", "。"], actual)
