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
    ret = 1
    for i in range(n - k + 1, n + 1):
        ret *= i
        ret %= mod

    for i in range(1, k + 1):
        ret *= pow(i, mod - 2, mod)
        ret %= mod

    return ret

def main():
    n,a,b = getList()
    ans = pow(2, n, MOD) - 1
    ans %= MOD
    # print(ans)
    ca = combmod(n,a)
    cb = combmod(n,b)
    ans += MOD
    ans -= (ca+cb)
    ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()

