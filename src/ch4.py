import MeCab
from packages import preprocess

# 形態素解析
wakati = MeCab.Tagger("-Owakati")
test = wakati.parse("pythonが大好きです").split()
print(test)

tagger = MeCab.Tagger()
test2 = tagger.parse("pythonが大好きです")
print([tmp.split("\t") for tmp in test2.split("\n")])

neologd = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
test3 = neologd.parse("8月3日に放送された「中居正広の金曜日のスマイルたちへ」(TBS系)で、ダイエット方法を紹介").split()
print(test3)

# 単語の正規化
text = "2万0689・24ドル"
print(preprocess.normalize_number(text))

text = "2万0689・24ドル"
print(preprocess.normalize_exact_number(text))
