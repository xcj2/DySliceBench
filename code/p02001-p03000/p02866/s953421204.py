# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template


def main():
    N = ii()
    a = lmi()
    if a[0] != 0:
        exit(0)

    a.sort()
    ma = max(a)
    if a[1] == 0:
        exit(0)
    ans = 1
    dp = [0] * N
    for x in a:
        dp[x] += 1
    for i in range(1, ma + 1):
        ans = ans * pow(dp[i - 1], dp[i], 998244353) % 998244353
    print(ans)
    return


if __name__ == '__main__':
    main()
