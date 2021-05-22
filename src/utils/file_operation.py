import os
import urllib.request


def download_file(url, filepath):
    """ファイルのダウンロード

    Args:
        url (str): ファイルダウンロード先のURL
        filepath (str): ファイルパス
    """
    if os.path.exists(filepath):
        print("File already exists.")
    else:
        print("Downloading...")
        # url からファイルをダウンロードし、指定したパスにファイルを保存する
        urllib.request.urlretrieve(url, filepath)
