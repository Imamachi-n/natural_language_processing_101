# natural_language_processing_101

機械学習・深層学習による自然言語処理入門の写経用リポジトリ

## Get started

### Python のインストール

```zsh
brew install pyenv

# 設定ファイルに pyenv の初期化処理を入れて、コンソールをリロード
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec $SHELL -l
```

### Python の特定バージョンの設定

```zsh
# バージョンリストを出して、最新のバージョンを探す
pyenv install -l

# anaconda-3 をインストールして、global の python として指定
# MEMO: anaconda3-2020.11 は一例
pyenv install anaconda3-2020.11
pyenv global anaconda3-2020.11
```

### pyenv のインストール

```zsh
brew install pipenv
```

### 必要なパッケージのインストール

以下のコマンドを実行することで、`Pipfile.lock` を使ってインストールして環境を再現します。

```zsh
pipenv sync --dev    # 開発用パッケージもインストール
```

### Mecab - 形態素解析エンジンのインストール

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

### [参考] VSCode で pyenv のパッケージパスを通す

pyenv を使っていると、VSCode でのパッケージのインポートのエラーになる。  
`.vscode/settings.json` にパッケージのパスと python のパスを記述後、VSCode をリロード。

```json
{
  "python.venvPath": "/Users/<username>/.local/share/virtualenvs/<project_name>",
  "python.pythonPath": "/Users/<username>/.local/share/virtualenvs/<project_name>/bin/python"
}
```

## Jupyter-lab の起動

以下のコマンドを実行して、Juptyer-lab を起動する。

```zsh
pipenv run jlab
```
