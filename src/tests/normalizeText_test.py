import unittest

from src.packages import normalizeText


class TestCleanText(unittest.TestCase):

    def test_nomalize_number(self):
        actual = normalizeText.normalize_number("1000円札を拾った")
        self.assertEqual("0円札を拾った", actual)

    def test_nomalize_exact_number(self):
        actual = normalizeText.normalize_exact_number("1000円札を拾った")
        self.assertEqual("0000円札を拾った", actual)

    def test_normalize_unicode(self):
        actual = normalizeText.normalize_unicode("１1①アｱ")
        self.assertEqual("111アア", actual)
