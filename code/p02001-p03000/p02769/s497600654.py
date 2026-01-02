import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10 ** 20
MOD = 10**9 + 7
def combmod(n, k, mod=MOD):
    if k == 0:
        return 1
    if k == 1:
        return n
    ret = 1
    for i in range(n - k + 1, n + 1):
        ret *= i
        ret %= mod

    for i in range(1, k + 1):
        ret *= pow(i, mod - 2, mod)
        ret %= mod

    return ret

def main():
    n, k = getList()
    if k >= n-1:
        ans = combmod(n+n-1, n)
    else:
        # ans = 0
        ans = 1
        tmp = 1
        for i in range(1, k+1):
            tmp *= n-i
            tmp *= n + 1 - i
            tmp *= pow(i, MOD-2, MOD)
            tmp *= pow(i, MOD - 2, MOD)
            ans += tmp
            tmp %= MOD
            # tmp = combmod(n-1, i)
            # tmp *= combmod(n, i)
            # tmp %= MOD
            # ans += tmp
            ans %= MOD
        # ans = combmod(n, k+1)
        # print(ans)
        # ans *= combmod(k+k+1, k+1)
        # # ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()

