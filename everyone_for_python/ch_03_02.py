#  集合(set)
dice = {1, 2, 3, 4, 5, 6}
coin = {"表", "裏"}

# 和集合を得る
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}

prime_fib = prime | fib
print(prime_fib)

# 差集合の作成
even = {2, 4, 6, 8, 10}

odd_dice = dice - even
print(odd_dice)

# 交わりを得る
prefs = {"北海道", "青森", "秋田", "岩手"}
capitals = {"札幌", "青森", "秋田", "盛岡"}

pref_cap = prefs & capitals
print(pref_cap)

# 対称差の作成
pref_cap2 = prefs ^ capitals
print(pref_cap2)

# リストをsetに変換する
codon = ['ATG', 'GGC', 'TCC', 'AAG', 'TTC', 'TGG', 'GAC', 'TCC']
s_codon = set(codon)

print(len(codon), len(s_codon))

# 要素の検索とsetの比較
prime_fib = prime & fib
if 13 in prime_fib:
    print("13は素数で、フィボナッチ数でもある")
if {2, 3} <= prime_fib:
    print("２、３は素数で、フォボナッチ数でもある")
