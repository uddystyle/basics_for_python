# 文字列型を使いこなす
# replace()メソッドの例

import matplotlib.pyplot as plt
orig_str = "いっぱい"
str = orig_str.replace("い", "お")
print(str)

# 文字列の削除と数値への変換
str_num = "1,000,000"
num = int(str_num.replace(",", ""))
print(num)

# 文字列の分布とグラフ表示

str_speeds = "38 42 20 40 39"
str_armor = "80 50 17 50 51"
speeds = str_speeds.split(" ")
armors = str_armor.split(" ")
markers = ["o", "v", "^", "<", ">"]

for idx in range(len(speeds)):
    x = int(speeds[idx])
    y = int(armors[idx])
    plt.scatter(x, y, marker=markers[idx])

# 空白区切りをカンマ区切りにする
str_speeds = "38 42 20 40 39"
speeds = str_speeds.split()
csep_speeds = ",".join(speeds)
print(csep_speeds)

# 余分な空白を削除する
str_speeds2 = " 38 42 20 40 39 "
sep_str = str_speeds2.replace(" ", ",")
print(sep_str)

# 分割してから余分な空白を削除する
str_speeds2 = " 38 42 20 40 39 "
speeds2 = str_speeds2.split()
csep_speeds2 = ",".join(speeds2)
print(csep_speeds2)

# 関数内で改行を含む文字列を変数として定義する例


def func():
    words = """ゆく河の流れは絶えずして\nしかももとの水にあらず"""
    print(words)


func()


# フォーマットに文字列を差し込む
"{} loves Python !".format("Guido")

# 複数を同時に差し込む
linkstr = '<a href="{}">{}</a>'
for i in ['http://python.org',
          'http://pypy.org',
          'http://cython.org', ]:
    print(linkstr.format(i, i.replace('http://', '')))
