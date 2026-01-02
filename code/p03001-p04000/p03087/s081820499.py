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
    n, q = LI()
    s = 'X' + SI()
    Q = [LI() for _ in range(q)]

    ac = [0]
    for i in range(1, n + 1):
        if (s[i], s[i - 1]) == ('C', 'A'):
            ac.append(ac[-1] + 1)
        else:
            ac.append(ac[-1])

    for l, r in Q:
        print(ac[r] - ac[l])
    # return res


main()
