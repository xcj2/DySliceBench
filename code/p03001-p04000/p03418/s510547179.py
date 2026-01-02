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
    n, k = LI()

    if k == 0:
        print(n ** 2)
        return 0

    res = 0
    for b in range(1, n + 1):
        p, r = divmod(n, b)
        ok = max(0, b - k)
        res += ok * p + max(0, r - k + 1)

    print(res)


if __name__ == '__main__':
    main()
