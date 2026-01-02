# coding:utf-8

import sys
from collections import deque, Counter

INF = float('inf')
MOD = 10 ** 9 + 7
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    S = [SI() for _ in range(n)]

    cnt = {"B_": 0, "_A": 0, "B_A": 0}
    res = 0
    for s in S:
        for i in range(len(s) - 1):
            if s[i: i + 2] == 'AB':
                res += 1

        if s[0] == 'B' and s[-1] == 'A':
            cnt["B_A"] += 1
        elif s[0] == 'B':
            cnt["B_"] += 1
        elif s[-1] == 'A':
            cnt["_A"] += 1

    # print(res, cnt)
    res += min(cnt["B_"], cnt["_A"])
    if max(cnt["B_"], cnt["_A"]) > 0:
        res += cnt["B_A"]
    else:
        res += max(0, cnt["B_A"] - 1)

    print(res)


if __name__ == '__main__':
    main()