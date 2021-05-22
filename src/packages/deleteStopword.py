import os
import urllib.parse
import urllib.request


def download_jp_stopwords(path=""):
    """日本語のストップワードをダウンロードし、ストップワードのセットを取得

    Args:
        path (str, optional): 日本語のストップワードのファイルパス. Defaults to "".

    Returns:
        [set]: ストップワードのセット
    """
    if not path:
        data_dir = urllib.parse.urljoin(
            os.path.dirname(os.path.abspath(__file__)), "data"
        )
        path = data_dir + "/" + "jp_stopwords.txt"
    print(path)
    url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
    if os.path.exists(path):
        print("File already exists.")
    else:
        print("Downloading...")
        # url からファイルをダウンロードし、指定したパスにファイルを保存する
        urllib.request.urlretrieve(url, path)

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
