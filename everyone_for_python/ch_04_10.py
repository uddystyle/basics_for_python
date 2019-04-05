# Pythonの文字列と日本語
# バイト型を使う
s = "あいうえお"
print(len(s))

bs = s.encode("shift-jis")
print(len(bs))

print(bs)

print(s[0])

print(bs[0])

# バイト型に変換する
u = s.encode("euc-jp", "strict")
print(u)

# バイト型文字列に変換する
u = s.encode("shift-jis", "ignore")
print(u)

# エンコードの判定
# guess_encoding()関数


def guess_encoding(s):
    """
    バイト型の文字列を引数として受け取り、
    エンコードを簡易に判定する
    """
    # 判定を行うエンコードをリストに保存
    encodings = ["ascii", 'utf-8', 'shift-jis', 'euc-jp']
    for enc in encodings:
        try:
            s.decode(enc)
        except UnicodeDecodeError:
            continue
        else:
            return enc
            # エラーが発生しなかったら変換に成功したエンコードを返す
    else:
        # 成功したエンコードがなければから文字列を返す
        return ""
