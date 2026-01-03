# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, m = LI()

    B = [1] * n
    R = [0] * n
    R[0] = 1

    for _ in range(m):
        x, y = LI_()

        B[x] -= 1
        B[y] += 1

        # 赤いボールが移動したかも？
        if R[x]:
            R[y] = 1

        # 箱が空なので赤いボールは絶対入ってない！
        if not B[x]:
            R[x] = 0

    return sum(R)


print(main())
