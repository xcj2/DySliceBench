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
    n, k = LI()
    A = LI()

    # dp[i]: 石がi個の局面で1.勝つか0.負けるか
    dp = [0] * (k + 1)

    for i in range(k + 1):
        if not dp[i]:
            for a in A:
                if i + a > k:
                    continue
                dp[i + a] = 1
        # print(dp)

    return 'First' if dp[k] else 'Second'


print(main())
