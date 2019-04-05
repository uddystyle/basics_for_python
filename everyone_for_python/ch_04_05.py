# union()メソッド
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}

u = prime.union(fib)
print(u)

i = prime.intersection(fib)
print(i)

d = prime.difference(fib)
print(d)

s = prime.symmetric_difference(fib)
print(s)

a = prime.add(16)
print(a)

r = prime.remove(3)
print(r)
