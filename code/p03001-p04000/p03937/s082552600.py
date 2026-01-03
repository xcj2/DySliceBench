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
    h, w = LI()
    B = [SI() + '.' for _ in range(h)]
    B.append('.' * w)

    for y in range(h):
        for x in range(w):
            if B[y][x] == '.':
                continue
                
            # |# . .
            # |# # #
            # |# . #
            if B[y][x + 1] == '#' and B[y + 1][x] == '#':
                return 'Impossible'
            
            # |. . .
            # |. # .
            # |# # .
            # |. # #
            if min(y, x) != 0:
                if B[y - 1][x] == '.' and B[y][x - 1] == '.':
                    return 'Impossible'

    return 'Possible'


print(main())