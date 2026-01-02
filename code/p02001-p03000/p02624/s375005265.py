import math
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def main():
    n = I()
    ans = 0
    # 式変形より問題文を言い換える

    for j in range(1, n + 1):
        # 1 ~ n の中で j の倍数であるものの総和 の総和
        # 倍数の数
        k = n // j
        # 1 * j + 2 * j + ... + k * j
        ans += ((k + 1) * k // 2) * j
    print(ans)


main()
