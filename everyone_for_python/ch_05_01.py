# 関数型プログラミング
# 関数型プログラミングとは、全てを関数で済まそうとする手法
# 関数を使った処理
orig_str = "おかしがすきすきすがしかお"
"".join(reversed(orig_str)) == orig_str


tank_data = [("Ⅳ号戦車", 38, 80, 75), ("LT-38", 42, 50, 37),
             ("八九式中戦車", 20, 17, 57), ("Ⅲ号突撃砲", 40, 50, 75),
             ("M3中戦車", 39, 51, 75)]

tank_data.sort(key=lambda tup: sum(tup[1:4]), reverse=True)
print(tank_data)

# sorted()関数による書き換え
r = sorted(tank_data, key=lambda tup: sum(tup[1:4]), reverse=True)
print(r)
