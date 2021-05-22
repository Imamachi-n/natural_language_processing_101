import os
import urllib.parse

# データファイル保存先
DATA_DIRPATH = urllib.parse.urljoin(os.path.dirname(os.path.abspath(__file__)), "data")
SLOTHLAB_STOPWORD_FILEPATH = os.path.join(DATA_DIRPATH, "jp_stopwords.txt")
TEXT8_STOPWORD_FILEPATH = os.path.join(DATA_DIRPATH, "jp_text8.txt")

# ストップワードのリスト
SLOTHLAB_STOPWORD_URL = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
TEXT8_URL = "https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/ja.text8.zip"
