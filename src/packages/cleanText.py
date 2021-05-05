import re


def clean_text(text):
    # 空文字以外をリスト化 & 両端の空白を除く
    replaced_text_list = [str.strip() for str in text if str != ""]
    replaced_text = '\n'.join(replaced_text_list)  # 改行文字を除く(リストの連結)
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    # URLの除去
    replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
