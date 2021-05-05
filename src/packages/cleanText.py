import re


def clean_text(text):
    # 改行コードをあわせる & 両端の空白を除く
    replaced_text = '\n'.join(str.strip()
                              for str in text.splitlines() if str != "")
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    # URLの除去
    replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    return replaced_text
