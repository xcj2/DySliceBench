# coding:utf-8

import sys
import itertools

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    A = [II() for _ in range(5)]
    k = II()

    judge = True
    for x, y in itertools.combinations(A, 2):
        if y - x > k:
            judge = False
            break

    return 'Yay!' if judge else ':('


print(main())
