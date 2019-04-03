# タプルを使う
month_names = ("January", "February", "March", "April", "May", "June", "July")

print(month_names[1])
# month_names[0] = "睦月"

# タプルは入れ替えようとするとエラーになるが、タプル同士を足して新しいタプルはつくれる
month_names = month_names + \
    ("August", "September", "October", "November", "December")

print(month_names[11])

# タプルをキーとしたディクショナリの作成
pref_capitals = {(43.06417, 141.34694): "北海道(札幌)",
                 (40.82444, 140.74): "青森(青森市)",
                 (39.70361, 141.1525): "岩手県(盛岡市)"
                 }


# 指定した緯度、経度に合致する県庁所在地を調べる
loc = (39.70361, 141.1525)
for key in pref_capitals:
    if loc == key:
        print(pref_capitals[key])
        break


# 指定した緯度、経度に最も近い県庁所在地を調べる

loc = (41.768793, 140.72881)
nearest_cap = ''
nearest_dist = 10000
for key in pref_capitals:
    dist = (loc[0] - key[0]) ** 2 + (loc[1] - key[1]) ** 2
    if nearest_dist > dist:
        nearest_dist = dist
        nearest_cap = pref_capitals[key]

print(nearest_cap)
