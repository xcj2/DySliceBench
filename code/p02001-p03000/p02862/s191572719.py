from sys import stdin


def input():
    return stdin.readline()[:-1]


def intput():
    return int(input())


def sinput():
    return input().split()


def intsput():
    return map(int, sinput())


mod = 10 ** 9 + 7
def ncr(n, r):
    x = 1
    for i in range(n, r, -1):
        x *= i
        x %= mod
    for i in range(n - r, 1, -1):
        x *= pow(i, mod - 2, mod)
        x %= mod
    return x

x , y = intsput()

b = (2 * x - y) // 3
a = x - 2 * b

if a >= 0 and b >= 0 and a + 2 * b == x and 2 * a + b == y:
    print(ncr(a + b, b))
else:
    print(0)
