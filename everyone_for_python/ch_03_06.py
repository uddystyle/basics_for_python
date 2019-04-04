# 関数の応用
int("101010", 2)
# print(int())


# 関数にデフォルト引数を定義する
# FizzBuzzを解く関数
def fizzbuzz(count=100, fizzmod=3, buzzmod=5):
    for cnt in range(1, count+1):
        if cnt % fizzmod == 0 and cnt % buzzmod == 0:
            print("Fizzbuzz")
        elif cnt % fizzmod == 0:
            print('Fizz')
        elif cnt % buzzmod == 0:
            print("Buzz")
        else:
            print(cnt)


print(fizzbuzz())


# 関数の外側で定義した変数を関数内で使う
local_var = 1


def test_func(an_arg):
    local_var = an_arg
    print("test_func()の中 = ", local_var)


test_func(200)
print("test_func()の中 = ", local_var)
