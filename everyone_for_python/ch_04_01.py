# オブジェクトとしての組み込み型
# リストのインデックスを返す関数find_indexの定義


def find_index(the_list, target):
    idx = 0
    for item in the_list:
        if target == item:
            return idx
        idx = idx + 1


mcz = ["れに", "かなこ", "しおり", "あやか", "ももか"]
print(find_index(mcz, "しおり"))

print(mcz.index("しおり"))
