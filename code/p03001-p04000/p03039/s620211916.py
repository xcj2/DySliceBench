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
    n, m, k = getList()
    ans = 0
    mul = combmod(n*m-2, k-2)
    for i in range(0, n):
        for j in range(0, m):
            tmp = (j+i) * (n-i) * (m-j) * mul
            if i != 0 and j != 0:
                tmp *= 2
            ans += tmp
            ans %= MOD
            # print(ans,mul)

    print(ans)
if __name__ == "__main__":
    main()

