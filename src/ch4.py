import MeCab

wakati = MeCab.Tagger("-Owakati")
test = wakati.parse("pythonが大好きです").split()
print(test)

tagger = MeCab.Tagger()
test2 = tagger.parse("pythonが大好きです")
print([tmp.split("\t") for tmp in test2.split("\n")])
