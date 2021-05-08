import re
import unicodedata
import nltk
from nltk.corpus import wordnet


def normalize(text):
    """テキストの正規化（数字、）

    Args:
        text (string): テキスト

    Returns:
        [string]: 正規化済みのテキスト
    """
    normalized_text = normalize_unicode(text)
    normalized_text = normalize_number(normalized_text)
    normalized_text = lower_text(normalized_text)
    return normalized_text


def normalize_number(text):
    """数字の正規化

    Args:
        text (string): テキスト

    Returns:
        [string]: 数字を 0 に置換したテキスト(桁数がいくつあっても 0 に強制置換)
    """
    return re.sub(r'\d+', '0', text)


def normalize_exact_number(text):
    """数字の正規化（桁数は維持する）

    Args:
        text (string): テキスト

    Returns:
        [string]: 数字を 0 に置換したテキスト(桁数は維持）
    """
    return re.sub(r'\d', '0', text)


def normalize_unicode(text, form='NFKC'):
    """UNICODE の正規化

    Args:
        text (string): テキスト
        form (string), optional): 正規化形式. Defaults to 'NFKC'.

    Returns:
        string: UNICODE正規化したテキスト
    """
    return unicodedata.normalize(form, text)


def lower_text(text):
    """テキストの小文字化

    Args:
        text (string): テキスト

    Returns:
        [string]: 大文字を小文字化したテキスト
    """
    return text.lower()


# TODO: 後で確認 - 日本語に対応できるか調査
def lemmatize_term(term, pos=None):
    """類義語を正規化

    Args:
        term (string): 単語
        pos ([type], optional): [description]. Defaults to None.

    Returns:
        string: 正規化した単語
    """
    if pos is None:
        synsets = wordnet.synsets(term)
        if not synsets:
            return term
        pos = synsets[0].pos()
        if pos == wordnet.ADJ_SAT:
            pos = wordnet.ADJ
    return nltk.WordNetLemmatizer().lemmatize(term, pos=pos)
