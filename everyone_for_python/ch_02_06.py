# if文で条件分岐する
# if文の例（４つの２で１０を作る）

if 2 * 2 * 2 + 2 == 10:
    print("2*2*2+2は10")
if 2 + 2 * 2 + 2 == 10:
    print("2+2*2+2は10")
if (2 + 2) * 2 + 2 == 10:
    print("(2+2)*2+2は10")

# 数値を比較する
if 1 == 1:
    print("１番目はTrue")
if 5 ^ (4 - 4) + 9 == 10:
    print("２番目はTrue")
if 2 < len([0, 1, 2]):
    print("３番目はTrue")
if sum([1, 2, 3, 4]) < 10:
    print("４番目はTrue")

# 文字列を比較する
if "AUG" == "AUG":
    print("１番目はTrue")
if "AUG" == 'aug':
    print("２番目はTrue")
if "あいう" == "あいう":
    print("３番目はTrue")

# 文字列を検索する
# in演算子の使用例
if "GAG" in "AUGACGGAGCUU":
    print("１番目はTrue")
if "恋と戦いはあらゆるところが正当化されるのよ" in "正当化":
    print("２番目はTrue")
if "stumble" in "A horse may stumble though he has four legs":
    print("３番目はTrue")

# リストを比較する
# リストを比較する条件式の例
if [1, 2, 3, 4] == [1, 2, 3, 4]:
    print("１番目はTrue")
if [1, 2, 3] == [2, 3]:
    print("２番目はTrue")
if [1, 2, 3] == ['1', '2', '3']:
    print("３番目はTrue")

# リスト内の要素を調べる条件式の例
if 2 in [2, 3, 5, 7, 11]:
    print("１番目はTrue")
if 21 in [13, 17, 19, 23, 29]:
    print("２番目はTrue")
if 'アッサム' in ['ダージリン', 'アッサム', 'オレンジペコ']:
    print("３番目はTrue")


# else文を使う
if 2 ^ 3 - 2 + 4 == 10:
    print("式は１０")
else:
    print("式は１０にならない")
if 2 ** 3 - 2 + 4 == 10:
    print("式２は１０")
else:
    print("式２は１０にならない")

# ２重のif文を使用した例
a_year = 2080
if a_year >= 1993:
    if a_year == 1993:
        print(a_year, "年、れに誕生日")
    else:
        print(a_year, "年、れに", a_year-1993, "歳")

# elif文の使用例
a_year = 2080
if a_year == 1993:
    print(a_year, "年、れに誕生")
elif a_year > 1993:
    print(a_year, "年、れに", a_year-1993, "歳")

# for文とif文を組み合わせた例
a_num = 57
for num in range(2, a_num):
    if a_num % num == 0:
        print(a_num, "は素数ではありません。")
        break
