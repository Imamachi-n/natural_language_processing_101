import re


def clean_text(text):
    """自然言語処理を行う上で余計な文字を削除する

    Args:
        text (string): 文字列

    Returns:
        [string]: 前処理済みの文字列
    """
    # 改行コードをあわせる & 両端の空白を除く
    replaced_text = '\n'.join(str.strip()
                              for str in text.splitlines() if str != "")
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(
        r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', replaced_text)  # URLの除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    return replaced_text
