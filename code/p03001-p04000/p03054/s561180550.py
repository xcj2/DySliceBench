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
    h, w, n = LI()
    sr, sc = LI_()
    S = SI()
    T = SI()

    D = {0: ('L', 'R', -1), 1: ('R', 'L', 1), 2: ('U', 'D', -1), 3: ('D', 'U', 1)}
    is_drop = False
    for t in range(2):
        taka, aoki, d = D[t]
        x = sc
        for i in range(n):
            if S[i] == taka:
                x += d
                if x < 0 or x >= w:
                    is_drop = True
                    break
            if T[i] == aoki:
                x -= d
                if x < 0:
                    x = 0
                if x >= w:
                    x = w - 1

    for t in range(2, 4):
        taka, aoki, d = D[t]
        y = sr
        for i in range(n):
            if S[i] == taka:
                y += d
                if y < 0 or y >= h:
                    is_drop = True
                    break
            if T[i] == aoki:
                y -= d
                if y < 0:
                    y = 0
                if y >= h:
                    y = h - 1

    print('NO' if is_drop else 'YES')



if __name__ == '__main__':
    main()