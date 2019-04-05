# 関数と組み込み型
def foo(a, b, *vals):
    print(a, b, vals)


foo(1, 2, 3, 4, 5)

# 未定義のキーワード引数を受け取る


def bar(a, b, **args):
    print(a, b, args)


bar(1, 2, c=3, d=4)
