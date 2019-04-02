# loop
mcz = ["れに", "かなこ", "しおり", "あやか", "ももか"]
for member in mcz:
    print(member)

# リストの中身を確認する
print(mcz)


# 分散と標準偏差を計算する
# リストの値と平均との差を２乗して足す
# 全ての値について１を繰り返す
# 上で得た合計を要素数で割る

# 分散を計算する
monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total / length
variance = 0

for height in monk_fish_team:
    variance += (height - mean) ** 2

variance = variance / length
# print(variance)

# 標準偏差の計算
print(variance**0.5)

# 別のリストの標準偏差を計算する
volleyball_team = [143, 167, 170, 165]

total2 = sum(volleyball_team)
length2 = len(volleyball_team)
mean2 = total2 / length2
variance2 = 0

for height in volleyball_team:
    variance2 += (height - mean2) ** 2

variance2 = variance2 / length2
# print(variance2)

# 標準偏差の計算
print(variance2**0.5)

# range関数
for cnt in range(10):
    print(cnt)

# 複利計算の例（１５年間）
savings = 100
for i in range(15):
    savings += savings * 0.05

print(savings)
