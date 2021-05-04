# natural_language_processing_101

機械学習・深層学習による自然言語処理入門の写経用リポジトリ

<!-- TOC -->

- [natural_language_processing_101](#natural_language_processing_101)
  - [Get started](#get-started)
    - [Python のインストール](#python-のインストール)
    - [Python の特定バージョンの設定](#python-の特定バージョンの設定)
    - [pyenv のインストール](#pyenv-のインストール)
    - [必要なパッケージのインストール](#必要なパッケージのインストール)
    - [新しいパッケージの追加](#新しいパッケージの追加)
    - [Mecab - 形態素解析エンジンのインストール](#mecab---形態素解析エンジンのインストール)
      - [mecab-ipadic-NEologd - Web 上の言語資源から得た新語の追加](#mecab-ipadic-neologd---web-上の言語資源から得た新語の追加)
    - [[参考] VSCode で pyenv のパッケージパスを通す](#参考-vscode-で-pyenv-のパッケージパスを通す)
  - [Jupyter-lab のセットアップ](#jupyter-lab-のセットアップ)
    - [Jupyter-lab の起動](#jupyter-lab-の起動)
    - [Jupyter-lab にモジュールのパスを追加する](#jupyter-lab-にモジュールのパスを追加する)
  - [参考文献](#参考文献)

<!-- /TOC -->

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

### 新しいパッケージの追加

以下のコマンドを実行することで、プロジェクトの python 環境に特定のパッケージをインストール & 追加できます。

```zsh
pipenv install <package_name>
```

### Mecab - 形態素解析エンジンのインストール

Mac の場合、以下の通り Mecab をインストール(`pipenv sync` をやっていれば、やらなくても OK)

```zsh
pipenv install mecab-python3
```

※ `mecab-python3` パッケージ内に MeCab が含まれているため、以下のインストールはいらないかも？（ただし、ディクショナリは入っていないので別途インストールが必要）

```zsh
# Mecab / IPA の辞書のインストール
$ brew install mecab
$ brew install mecab-ipadic

# シェルを再起動して、インストールチェック
$ exec $SHELL -l
$ mecab --version
mecab of 0.996
```

#### mecab-ipadic-NEologd - Web 上の言語資源から得た新語の追加

以下のコマンドから、NEologd をインストールする。

```zsh
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
sudo bin/install-mecab-ipadic-neologd -n
```

mecab で NEologd の辞書のパスを指定する必要があるため、以下のコマンドでパスをチェック。

```zsh
echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
```

デフォルトだと、`/usr/local/lib/mecab/dic/mecab-ipadic-neologd` に保存される模様。

python で使用する場合は、以下のように辞書を指定する。

```python
import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
```

詳しくは、こちらの README を参照のこと。

- [mecab-ipadic-NEologd : Neologism dictionary for MeCab](https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md)

### [参考] VSCode で pyenv のパッケージパスを通す

pyenv を使っていると、VSCode でのパッケージのインポートのエラーになる。  
`.vscode/settings.json` にパッケージのパスと python のパスを記述後、VSCode をリロード。

```json
{
  "python.venvPath": "/Users/<username>/.local/share/virtualenvs/<project_name>",
  "python.pythonPath": "/Users/<username>/.local/share/virtualenvs/<project_name>/bin/python"
}
```

## Jupyter-lab のセットアップ

### Jupyter-lab の起動

以下のコマンドを実行して、Juptyer-lab を起動する。

```zsh
pipenv run jlab
```

### Jupyter-lab にモジュールのパスを追加する

以下のディレクトリ構成の場合で、`notebooks` ディレクトリに格納されている Jupyter Notebook から、
`packages` 内のモジュールにアクセスしたいケースを想定する。

```text
/
├── src/                # ソースコードのルートパス
     ├── notebooks/     # Jupyter Notebook のディレクトリ
     ├── packages/      # 各種パッケージ群
```

上記の構成の場合、以下の通りに `src` ディレクトリにパスを通す。

```python
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent))
```

`src` ディレクトリが Jupyter lab のモジュールパスが通っているので、`src` 起点でモジュールを読み込むことができる。

```python
from packages import preprocess
```

## 参考文献

-[【Python】形態素解析エンジン MeCab の使い方](https://hibiki-press.tech/python/mecab/5153)
