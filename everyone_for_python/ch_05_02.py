# 内包表記
# リスト内包表記の例
monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total / length

print(mean)

variance = sum([(height-mean)**2 for height in monk_fish_team])/length
print(variance)
print([(height-mean)**2 for height in monk_fish_team])

# リストの内包表記で書き換えたコード
str_speeds = "38 42 20 40 39"
speeds = [int(s) for s in str_speeds.split()]
print(speeds)

# リスト内表記でifを利用する
# 数字以外を排除してリストを作成
str_speeds = "38 42 20 40 a1 39"
speeds = [int(s) for s in str_speeds.split() if s.isdigit()]
print(speeds)

# ディクショナリ内包表記を使う
tz = {"GMT": "+000", "BST": "+100",
      "EET": "+200", "JST": "+900"}

revtz = {off: zone for zone, off in tz.items()}
print(revtz)

# set内包表記を使う
names = ["BOB", "burton", "dave", "bob"]
unames = {x.lower() for x in names}
print(unames)
