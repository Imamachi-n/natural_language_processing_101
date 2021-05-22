import MeCab

from packages import normalizeText, deleteStopword

# 形態素解析
wakati = MeCab.Tagger("-Owakati")
test = wakati.parse("pythonが大好きです").split()
print(test)

tagger = MeCab.Tagger()
test2 = tagger.parse("pythonが大好きです")
print([tmp.split("\t") for tmp in test2.split("\n")])

neologd = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
test_txt = "8月3日に放送された「中居正広の金曜日のスマイルたちへ」(TBS系)で、ダイエット方法を紹介"
test3 = neologd.parse(test_txt).split()
test4 = wakati.parse(test_txt).split()
print(test3)
print(test4)


# 単語の正規化
text = "2万0689・24ドル"
print(normalizeText.normalize_number(text))

text = "2万0689・24ドル"
print(normalizeText.normalize_exact_number(text))

# ストップワードの削除
test_stopword = wakati.parse("りんごをいくつか買う。").split()
stopword_list = deleteStopword.download_jp_stopwords()
print(deleteStopword.delete_stopwords(test_stopword, stopword_list))
