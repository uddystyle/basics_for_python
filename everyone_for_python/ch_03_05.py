# ループの応用
# FizzBuzz
from random import randint
cnt = 1
while cnt <= 100:
    if cnt % 3 == 0 and cnt % 5 == 0:
        print("FizzBuzz")
    elif cnt % 3 == 0:
        print("Fizz")
    elif cnt % 5 == 0:
        print("Buzz")
    else:
        print(cnt)
    cnt += 1


# じゃんけんプログラム
# break文、continue文を使うをループの流れを制御できる
hands = {0: "グー", 1: "チョキ", 2: "パー"}
rules = {(0, 0): "あいこ", (0, 1): "勝ち", (0, 2): "負け",
         (1, 0): "負け", (1, 1): "あいこ", (1, 2): "勝ち",
         (2, 0): "勝ち", (2, 1): "負け", (2, 2): "あいこ"}

while True:
    pc_hand = randint(0, 2)
    user_hand_str = input("0: グー 1: チョキ 2: パー 3: やめる")
    if user_hand_str == "3":
        break
    if user_hand_str not in ("0", "1", "2"):
        continue
    user_hand = int(user_hand_str)
    print("あなた" + hands[user_hand] + ", コンピューター:" + hands[pc_hand])
    print(rules[user_hand, pc_hand])

# for文とelse文の組み合わせ
a_num = 59
for num in range(2, a_num):  # ２からa_num-1まで繰り返す
    if a_num % num == 0:    # a_numをnumで割り切れるか
        print(a_num, "は素数ではありません")
        break

else:
    print(a_num, "は素数です")  # break文を一度も通らないでループが終了した。
