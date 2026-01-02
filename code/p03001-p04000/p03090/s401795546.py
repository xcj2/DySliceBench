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
    n = II()

    res = []
    for i in range(1, n + 1):
        for j in range(1 + i, n + 1):
            if i + j == n + (n % 2 == 0):
                continue
            res.append((i, j))

    print(len(res))
    for r in res:
        print(*r)


main()
