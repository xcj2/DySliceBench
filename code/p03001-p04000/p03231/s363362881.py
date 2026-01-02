import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    n, m = map(int, input().split())
    s = input()
    t = input()

    L = lcm(n, m)

    X = dict()
    for i in range(n):
        idx = (L // n) * i
        X[idx] = s[i]

    for i in range(m):
        idx = (L // m) * i
        if X.get(idx) != None and X[idx] != t[i]:
            print("-1")
            break
    else:
        print(L)


if __name__ == '__main__':
    resolve()
