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
      - [トラブルシューティング - 依存解決できない](#%E3%83%88%E3%83%A9%E3%83%96%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0---%E4%BE%9D%E5%AD%98%E8%A7%A3%E6%B1%BA%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84)
      - [トラブルシューティング - Big Sur 固有のトラブル](#%E3%83%88%E3%83%A9%E3%83%96%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0---big-sur-%E5%9B%BA%E6%9C%89%E3%81%AE%E3%83%88%E3%83%A9%E3%83%96%E3%83%AB)
  - [Mecab - 形態素解析エンジンのインストール](#mecab---%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [mecab-ipadic-NEologd - Web 上の言語資源から得た新語の追加](#mecab-ipadic-neologd---web-%E4%B8%8A%E3%81%AE%E8%A8%80%E8%AA%9E%E8%B3%87%E6%BA%90%E3%81%8B%E3%82%89%E5%BE%97%E3%81%9F%E6%96%B0%E8%AA%9E%E3%81%AE%E8%BF%BD%E5%8A%A0)
  - [VSCode のセットアップ](#vscode-%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)
    - [VSCode で pyenv の各種パスを通す](#vscode-%E3%81%A7-pyenv-%E3%81%AE%E5%90%84%E7%A8%AE%E3%83%91%E3%82%B9%E3%82%92%E9%80%9A%E3%81%99)
    - [VSCode に black を導入してオートフォーマットできるようにする](#vscode-%E3%81%AB-black-%E3%82%92%E5%B0%8E%E5%85%A5%E3%81%97%E3%81%A6%E3%82%AA%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB%E3%81%99%E3%82%8B)
    - [[オプション] VSCode に autopep8 を 導入してオートフォーマットできるようにする](#%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3-vscode-%E3%81%AB-autopep8-%E3%82%92-%E5%B0%8E%E5%85%A5%E3%81%97%E3%81%A6%E3%82%AA%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB%E3%81%99%E3%82%8B)
    - [mypy を使って VSCode 上で型を静的解析する](#mypy-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6-vscode-%E4%B8%8A%E3%81%A7%E5%9E%8B%E3%82%92%E9%9D%99%E7%9A%84%E8%A7%A3%E6%9E%90%E3%81%99%E3%82%8B)
    - [isort を使ってパッケージの並び順を揃える](#isort-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E4%B8%A6%E3%81%B3%E9%A0%86%E3%82%92%E6%8F%83%E3%81%88%E3%82%8B)
    - [オススメの VSCode 拡張機能をインストール](#%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1%E3%81%AE-vscode-%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [Jupyter-lab のセットアップ](#jupyter-lab-%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)
    - [Jupyter-lab の起動](#jupyter-lab-%E3%81%AE%E8%B5%B7%E5%8B%95)
    - [Jupyter-lab にモジュールのパスを追加する](#jupyter-lab-%E3%81%AB%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%AE%E3%83%91%E3%82%B9%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B)
  - [単体テスト](#%E5%8D%98%E4%BD%93%E3%83%86%E3%82%B9%E3%83%88)
    - [コマンドでの実行方法](#%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%A7%E3%81%AE%E5%AE%9F%E8%A1%8C%E6%96%B9%E6%B3%95)
    - [単体テストの書き方](#%E5%8D%98%E4%BD%93%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E6%9B%B8%E3%81%8D%E6%96%B9)
  - [自然言語処理のメモ](#%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E3%81%AE%E3%83%A1%E3%83%A2)
    - [こちらへ](#%E3%81%93%E3%81%A1%E3%82%89%E3%81%B8)
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

# 別の例
pyenv install 3.9.4
pyenv global 3.9.4
```

### pipenv のインストール

このプロジェクトでは、`pipenv` というパッケージ管理ツールを使っています。  
Mac では以下のコマンドで `pipenv` をインストールします。

```zsh
brew install pipenv
PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.9.4
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

#### トラブルシューティング - 依存解決できない

例えば、`ERROR: Could not find a version that matches keras-nightly~=2.5.0.dev` のようなエラーが出ている場合、`pre-release` のパッケージに依存していることが原因で依存解決ができないらしい。

なので、以下の方法で `pre-release` のパッケージをインストールできるようにする。

```zsh
# いったん、lock ファイルを削除
pipenv lock --clear

# pre-release に依存している場合、以下のコマンドで問題なくインストールできるはず
pipenv lock --pre
```

#### トラブルシューティング - Big Sur 固有のトラブル

例えば、MacOS で Big Sur を使っている状況で、`ERROR: Could not find a version that matches tensorflow` のようなエラーが出た場合、以下の環境変数を設定した後、`pipenv install` をする。

コンパチブルモード（Big Sur（11 系）であっても OS のバージョンを 10 系列として振る舞う）でコマンドを実行できる。

```zsh
export SYSTEM_VERSION_COMPAT=1
pipenv install
```

参考 Issue は[こちら](https://github.com/pypa/pipenv/issues/4578)。

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

### VSCode に black を導入してオートフォーマットできるようにする

`black` をインストールします。

```zsh
pipenv install --dev black
```

デフォルトの formatter が Prettier などになっていると、フォーマットエラーになります。
`.vscode/settings.json` に python の場合のデフォルトの formatter を設定する必要があります。

```json
{
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  },
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "black"
}
```

### [オプション] VSCode に autopep8 を 導入してオートフォーマットできるようにする

※ black のほうが個人的に好きなのでおすすめ。
`flake8` と `autopep8` に関連するパッケージをインストールします。

```zsh
pipenv install --dev flake8 flake8-import-order autopep8
```

デフォルトの formatter が Prettier などになっていると、フォーマットエラーになります。
`.vscode/settings.json` に python の場合のデフォルトの formatter を設定する必要があります。
その上で、`autopep8` の設定などを追加します。

```json
{
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  },
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8",
  "python.formatting.autopep8Path": "${workspaceFolder}/.venv/bin/autopep8"
}
```

### mypy を使って VSCode 上で型を静的解析する

`mypy` をまずインストールします。

```zsh
pipenv install --dev mypy
```

VSCode の設定ファイル `.vscode/settings.json` に以下の設定を追加します。

```json
{
  "python.linting.mypyEnabled": true
}
```

### isort を使ってパッケージの並び順を揃える

`isort` をインストールします。

```zsh
pipenv install --dev isort
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

## 単体テスト

### コマンドでの実行方法

以下のコマンドで `src/tests` ディレクトリにある `*_test.py` ファイルのテストを実行します。  
このコマンドを `pipenv` の `scripts` に登録し、実行すると便利です。

```zsh
python -m unittest discover src/tests -p '*_test.py' -v
```

### 単体テストの書き方

以下を参照。

- [Python 標準の unittest の使い方メモ](https://qiita.com/aomidro/items/3e3449fde924893f18ca)
- [Python 3 標準の unittest でテストを書く際のディレクトリ構成](https://qiita.com/hoto17296/items/fa0166728177e676cd36)
- [unittest --- ユニットテストフレームワーク](https://docs.python.org/ja/3/library/unittest.html)

## 自然言語処理のメモ

### [こちらへ](./docs/README.md)

## 参考文献

- [【Python】形態素解析エンジン MeCab の使い方](https://hibiki-press.tech/python/mecab/5153)
- [VSCode の Python 開発環境で pylint の代わりに flake8 を導入し自動整形を設定する](https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb)
- [Windows + Python + PipEnv + Visual Studio Code で Python 開発環境](https://qiita.com/youkidkk/items/b674e6ace96eb227cc28)
- [Pipenv で仮想環境をプロジェクトディレクトリ配下に作る方法](https://dev.classmethod.jp/articles/pipenv-venv-setting/)
- [Pipenv で flake8 / autopep8 を上手く使う](https://qiita.com/ciloholic/items/9de9391f8457dc9bc60c)
- [Python のコードを快適に書くための設定をまとめてみる](https://k2ss.info/archives/2976/)
- [How to correctly set formatter for python when formatter for other language enabled?](https://github.com/microsoft/vscode-docs/issues/3728)
- [python の開発環境を構築する](https://www.marsa-blog.com/2019/06/developpython1.html#p2-4)
