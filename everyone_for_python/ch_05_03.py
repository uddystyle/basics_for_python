# イテレータを使う
# read()メソッドでファイル全体を読み込む
f = open("some.txt")
body = f.read()
lines = body.split('\n')
print('\n'.join(lines[:5]))

# readline()メソッドで１行ずつ読み込む
f = open('some.txt')
lines = ''
for i in range(5):
    lines += f.readline()
print(lines)


# イテレータを使う
for c, l in enumerate(open('some.txt')):
    print(l, end='')
    if c == 4:
        break
