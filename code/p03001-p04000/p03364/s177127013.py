# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    B = [SI() for _ in range(n)]

    res = 0
    for i in range(n):
        is_good = 1
        for h in range(n):
            for w in range(h + 1, n):
                if B[h][(w + i) % n] != B[w][(h + i) % n]:
                    is_good = 0
                    break

            if not is_good:
                break

        if is_good:
            res += n

    return res


print(main())
