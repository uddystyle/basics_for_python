# for文と組み込み型
# range()関数を使いこなす
for i in range(10, 21):
    print(i, end=' \n')

# グローバル変数を定義しないでループをまわす
l = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(l):
    print(i, name)


# ２つのシーケンスを使ったループ
for n, w in zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']):
    print(n, w)
