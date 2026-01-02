# coding:utf-8

import sys
from collections import defaultdict

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
    A = LI()

    MA = defaultdict(int)
    # 目標値をO(1)で見つけるために辞書に格納
    for a in A:
        MA[a] += 1

    key_n = list(MA.keys())
    key_n.sort()
    key_n.reverse()

    res = 0
    p = 30
    for x in key_n:
        # すでにペアを作るために使用してしまっている時はパス
        if not MA[x]:
            continue

        # 残っているボールの中で一番大きな値xを選ぶと，そのボールを使って表せる2べきの値x + yは1つに定まる
        # x + 1 <= x + y < 2x
        # 2べきの比は2であるのに対して，x + 1と2xの比は2未満だから
        while 2 * x < 2 ** p:
            p -= 1

        if x + 1 <= 2 ** p:
            y = 2 ** p - x
            if not MA[y]:
                continue

            if x == y:
                _add = MA[x] // 2
            else:
                _add = min(MA[x], MA[y])

            res += _add
            MA[x] -= _add
            MA[y] -= _add

    print(res)


if __name__ == '__main__':
    main()
