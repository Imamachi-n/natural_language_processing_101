# natural_language_processing_101

機械学習・深層学習による自然言語処理入門の写経用リポジトリ

<!-- TOC -->

- [natural_language_processing_101](#natural_language_processing_101)
  - [環境構築 python のセットアップ](#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-python-%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)
    - [Python のインストール](#python-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
      - [Python の特定バージョンの設定](#python-%E3%81%AE%E7%89%B9%E5%AE%9A%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A)
    - [pipenv のインストール](#pipenv-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
      - [必要なパッケージのインストール](#%E5%BF%85%E8%A6%81%E3%81%AA%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
      - [新しいパッケージの追加](#%E6%96%B0%E3%81%97%E3%81%84%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E8%BF%BD%E5%8A%A0)
      - [パッケージ群の削除](#%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E7%BE%A4%E3%81%AE%E5%89%8A%E9%99%A4)
  - [Mecab - 形態素解析エンジンのインストール](#mecab---%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [mecab-ipadic-NEologd - Web 上の言語資源から得た新語の追加](#mecab-ipadic-neologd---web-%E4%B8%8A%E3%81%AE%E8%A8%80%E8%AA%9E%E8%B3%87%E6%BA%90%E3%81%8B%E3%82%89%E5%BE%97%E3%81%9F%E6%96%B0%E8%AA%9E%E3%81%AE%E8%BF%BD%E5%8A%A0)
  - [VSCode のセットアップ](#vscode-%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)
    - [VSCode で pyenv の各種パスを通す](#vscode-%E3%81%A7-pyenv-%E3%81%AE%E5%90%84%E7%A8%AE%E3%83%91%E3%82%B9%E3%82%92%E9%80%9A%E3%81%99)
    - [オススメの VSCode 拡張機能をインストール](#%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1%E3%81%AE-vscode-%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [Jupyter-lab のセットアップ](#jupyter-lab-%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)
    - [Jupyter-lab の起動](#jupyter-lab-%E3%81%AE%E8%B5%B7%E5%8B%95)
    - [Jupyter-lab にモジュールのパスを追加する](#jupyter-lab-%E3%81%AB%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%AE%E3%83%91%E3%82%B9%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B)
  - [参考文献](#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)

<!-- /TOC -->

## 環境構築 (python のセットアップ)

### Python のインストール

```zsh
brew install pyenv

# 設定ファイルに pyenv の初期化処理を入れて、コンソールをリロード
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec $SHELL -l
```

#### Python の特定バージョンの設定

```zsh
# バージョンリストを出して、最新のバージョンを探す
pyenv install -l

# anaconda-3 をインストールして、global の python として指定
# MEMO: anaconda3-2020.11 は一例
pyenv install anaconda3-2020.11
pyenv global anaconda3-2020.11
```

### pipenv のインストール

このプロジェクトでは、`pipenv` というパッケージ管理ツールを使っています。  
Mac では以下のコマンドで `pipenv` をインストールします。

```zsh
brew install pipenv
```

#### 必要なパッケージのインストール

以下のコマンドを実行することで、`Pipfile.lock` を使って環境を再現することができます。  
また、`PIPENV_VENV_IN_PROJECT=1` という環境変数を指定することで、
プロジェクトルート直下の `.venv` ディレクトリにパッケージを保存することができます。

```zsh
PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev    # 開発用パッケージもインストール
```

#### 新しいパッケージの追加

以下のコマンドを実行することで、プロジェクトの python 環境に特定のパッケージをインストール & 追加できます。

```zsh
pipenv install <package_name>
```

開発向けのパッケージをインストールする場合は、`--dev` オプションをつける。

```zsh
pipenv install --dev <package_name>
```

#### パッケージ群の削除

仮想環境のパッケージ群を削除するには、以下のコマンドを実行する。

```zsh
pipenv --rm
```

## Mecab - 形態素解析エンジンのインストール

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

### mecab-ipadic-NEologd - Web 上の言語資源から得た新語の追加

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

## VSCode のセットアップ

VSCode を使っている場合、以下の設定を行う必要があります。

### VSCode で pyenv の各種パスを通す

pyenv を使っていると、VSCode でのパッケージのインポートのエラーになる。  
`.vscode/settings.json` にパッケージのパスと python のパスを記述後、VSCode をリロード。

```json
{
  "python.venvPath": "${workspaceFolder}/.venv",
  "python.autoComplete.extraPaths": [
    "${workspaceFolder}/.venv/Lib/site-packages"
  ],
  "python.pythonPath": "${workspaceFolder}/.venv/bin/python"
}
```

### オススメの VSCode 拡張機能をインストール

`.vscode/extensions.json` におすすめの拡張機能をリストアップしてあるので、必要に応じてインストールする。  
（全てのオススメ拡張機能をインストールするかどうか、ポップアップで最初に聞かれるはず）

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

- [【Python】形態素解析エンジン MeCab の使い方](https://hibiki-press.tech/python/mecab/5153)
- [VSCode の Python 開発環境で pylint の代わりに flake8 を導入し自動整形を設定する](https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb)
- [Windows + Python + PipEnv + Visual Studio Code で Python 開発環境](https://qiita.com/youkidkk/items/b674e6ace96eb227cc28)
- [Pipenv で仮想環境をプロジェクトディレクトリ配下に作る方法](https://dev.classmethod.jp/articles/pipenv-venv-setting/)
- [Pipenv で flake8 / autopep8 を上手く使う](https://qiita.com/ciloholic/items/9de9391f8457dc9bc60c)
