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
    B = LI()

    res = []
    T = B[:]
    for _ in range(n):
        for i in range(len(T))[::-1]:
            if i + 1 == T[i]:
                res.append(T[i])
                T = T[:i] + T[i+1:]
                break
        else:
            print(-1)
            return 0

    print(*[i for i in reversed(res)], sep='\n')
    return 1


main()
