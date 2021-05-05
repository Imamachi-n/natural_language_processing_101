import re


def normalize_number(text):
    return re.sub(r'\d+', '0', text)


def normalize_exact_number(text):
    return re.sub(r'\d', '0', text)


if __name__ == '__main__':
    print("これは自作モジュールです")
