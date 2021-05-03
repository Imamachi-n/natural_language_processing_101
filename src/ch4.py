import MeCab

wakati = MeCab.Tagger("-Owakati")
test = wakati.parse("pythonが大好きです").split()
print(test)

tagger = MeCab.Tagger()
test2 = tagger.parse("pythonが大好きです")
print([tmp.split("\t") for tmp in test2.split("\n")])

neologd = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
test3 = neologd.parse("8月3日に放送された「中居正広の金曜日のスマイルたちへ」(TBS系)で、ダイエット方法を紹介").split()
print(test3)
