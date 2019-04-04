# リスト型、タプル型を使いこなす
# 昇順に並べる
monk_fish_team = [158, 157, 163, 157, 145]
monk_fish_team.sort()
print(monk_fish_team)


# 降順に並べる
monk_fish_team.sort(reverse=True)
print(monk_fish_team)

# タプルのリストを作る
tank_data = [("Ⅳ号戦車", 38, 80, 75), ("LT-38", 42, 50, 37),
             ("八九式中戦車", 20, 17, 57), ("Ⅲ号突撃砲", 40, 50, 75),
             ("M3中戦車", 39, 51, 75)]


def evaluate_tankdata(tup):
    return tup[1] + tup[2] + tup[3]


print(evaluate_tankdata(tank_data[0]))
print(evaluate_tankdata(tank_data[4]))


# 戦車の強さでソートする
tank_data.sort(key=evaluate_tankdata, reverse=True)
print(tank_data)


# アンパックを使う
a = 1
b = 2
b, a = a, b
print(a, b)


# リストからスライスで要素を取り出す
a = [1, 2, 3, 4, 5]
print(a)
print(a[1:4])
print(a[2:100])
print(a[::2])

# 要素の追加
a = [1, 2, 3, 4, 5]
a[2:4] = ['Three', 'Four', 'Five']
print(a)

# 要素の削除
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)
