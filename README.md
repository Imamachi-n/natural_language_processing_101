# natural_language_processing_101

機械学習・深層学習による自然言語処理入門の写経用リポジトリ

## Get started

以下のコマンドを実行することで、`Pipfile.lock` を使ってインストールして環境を再現します。

```zsh
pipenv sync --dev    # 開発用パッケージもインストール
```

## Mecab - 形態素解析エンジンのインストール

Mac の場合、以下の通り Mecab をインストール

```zsh
# Mecab / IPA の辞書のインストール
$ brew install mecab
$ brew install mecab-ipadic

# シェルを再起動して、インストールチェック
$ exec $SHELL -l
$ mecab --version
mecab of 0.996
```

## Jupyter-lab の起動

以下のコマンドを実行して、Juptyer-lab を起動する。

```zsh
pipenv run jlab
```
