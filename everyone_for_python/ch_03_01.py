# ディクショナリをつかう
purple = {"ニックネーム": "れにちゃん", "出身地": "神奈川県", "キャッチフレーズ": "感電少女"}
print(purple["出身地"])

# キーを使って要素を入れ替える
purple["キャッチフレーズ"] = "鎖少女"
print(purple)

# 新しい要素を追加する
purple["生年月日"] = "1996年6月31日"
print(purple)

# キーを使って要素を削除する
del purple["ニックネーム"]
print(purple)

# キーの存在確認


def convert_member(num):
    # アラビア数字とローマ数字の対応表をディクショナリに定義
    roman_nums = {1: "Ⅰ", 2: "Ⅱ", 3: "Ⅲ", 4: "Ⅳ",
                  5: "Ⅴ", 6: "Ⅵ", 7: "Ⅶ", 8: "Ⅷ", 9: "Ⅸ"}
    # ディクショナリのキーとして整数が存在していたら
    # キーに対応する値を戻り値にする
    if num in roman_nums:
        return roman_nums[num]
    else:
        return "[変換できません]"


print(convert_member(8))

for key in purple:
    print(key, purple[key])
