# coding:utf-8

import sys
INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    h, w = LI()

    if h % 3 == 0 or w % 3 == 0:
        return 0

    res = INF
    j = w // 2
    for i in range(1, h // 2 + 1):
        S = [i * w, (h - i) * j, (h - i) * (w - j)]
        res = min(res, max(S) - min(S))
        k = (h - i) // 2
        S = [i * w, k * w, ((h - i) - k) * w]
        res = min(res, max(S) - min(S))

    i = h // 2
    for j in range(1, w // 2 + 1):
        S = [j * h, (w - j) * i, (w - j) * (h - i)]
        res = min(res, max(S) - min(S))
        k = (w - j) // 2
        S = [j * h, k * h, ((w - j) - k) * h]
        res = min(res, max(S) - min(S))

    return res


print(main())
