# 関数をつかう
# リストの値を合計する
from random import randint
the_list = [101, 123, 152, 123]
summary = 0
for item in the_list:
    summary = summary + item

print(summary)


# 関数を呼び出す
print(abs(10))
print(abs(-200))

print(int("100"))
print(int("100", 2))
print(int("100", 16))

# 関数を定義する


def destiny_tank():
    tanks = ["IV号戦車D型", "III号戦車j型", "チャーチル MK.VII",
             "M4シャーマン", "P40重戦車", "T-34/76"]
    num = input("好きな数字を入力してください")
    idx = int(num) % len(tanks)
    print("あなたの運命の戦車は")
    print(tanks[idx])


# destiny_tank()

# 引数をもつ関数の定義


def destiny_tank2(num):
    tanks = ["IV号戦車D型", "III号戦車j型", "チャーチル MK.VII",
             "M4シャーマン", "P40重戦車", "T-34/76"]
    idx = num % len(tanks)
    print("あなたの運命の戦車は")
    print(tanks[idx])


# num_str = input("好きな数字を入力してください")
# num = int(num_str)
# destiny_tank2(num)


# num = randint(0, 10)
# destiny_tank2(num)

# 戻り値を持つ関数の定義


def destiny_tank3(num):
    tanks = ["IV号戦車D型", "III号戦車j型", "チャーチル MK.VII",
             "M4シャーマン", "P40重戦車", "T-34/76"]
    idx = num % len(tanks)
    return tanks[idx]


num = randint(0, 10)
tank = destiny_tank3(num)
print("今日あなたが乗るべき幸運の戦車は", tank, "です")

# ローカル変数


def test_func(arg1):
    inner_var = 100
    print(arg1 + inner_var)


test_func(10)
# print(inner_var)


# calc_variance()関数の定義
def calc_variance(a_list):
    total = sum(a_list)
    length = len(a_list)
    mean = total / length
    variance = 0

    for height in a_list:
        variance += (height - mean) ** 2
    variance = variance/len(monk_fish_team)

    return variance


monk_fish_team = [158, 157, 163, 157, 145]
volley_ball_team = [143, 167, 170, 165]
pravda_team = [127, 172, 140, 160, 174]

monk_fish_variance = calc_variance(monk_fish_team)
volley_ball_variance = calc_variance(volley_ball_team)
pravda_fish_variance = calc_variance(pravda_team)

print(monk_fish_variance**0.5)
print(volley_ball_variance**0.5)
print(pravda_fish_variance**0.5)
