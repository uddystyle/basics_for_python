# ファイルを開く
f = open("foo.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close()

# テキストファイルを行に分割する
f = open("test.txt", "r", encoding="utf-8")
for line in f:
    print(line, end=" ")

# モードを指定してファイルを開く
f = open("newfile.txt", "w", encoding="utf-8")
f.write(s)
f.close()

# バイナリファイルを開く
imgfile = open('someimage.png', 'rb')
imgsrc = imgfile.read()
if imgsrc[1:4] == b'PNG':
    print('image/png')
