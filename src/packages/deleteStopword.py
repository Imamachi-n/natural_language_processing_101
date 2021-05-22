from src.utils import constants
from src.utils import file_operation


def download_jp_stopwords():
    """日本語のストップワードをダウンロードし、ストップワードのセットを取得

    Returns:
        [set]: ストップワードのパス
    """
    path = constants.SLOTHLAB_STOPWORD_FILEPATH
    url = constants.SLOTHLAB_STOPWORD_URL
    file_operation.download_file(url, path)
    return path


def download_wiki_jp_data():
    """TEXT8 のファイルダウンロード

    Returns:
        str: ファイルパス
    """
    path = constants.TEXT8_STOPWORD_FILEPATH
    url = constants.TEXT8_URL
    file_operation.download_file(url, path)
    return path


def get_stopwords(path):
    """slothLib ファイルからストップワードのリストを取得

    Args:
        path (str): ファイルパス

    Returns:
        list: ストップワードのリスト
    """
    with open(path, "r", encoding="utf-8") as file:
        stopwords = [w.strip() for w in file.readlines()]
        return list(set(stopwords))


def delete_stopwords(words, stopwords):
    """ストップワードの除去

    Args:
        words (str): ワードのリスト
        stopwords (set): ストップワードのセット

    Returns:
        str[]: ストップワードを除去したワードリスト
    """
    return [w for w in words if w not in stopwords]


# TODO: 品詞と名詞をストップワードとして除去する処理を追加
def delete_simple_jp_stopwords(words):
    return


# https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/ja.text8.zip
