import sys
import time
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
import bisect
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**21

def routes_from_zero(r,c, factorial, gyaku):
    ret = 0
    for i in range(r + 1):
        tmp = 1
        tmp *= factorial[i+c+1]
        # tmp %= MOD
        tmp *= gyaku[c]
        # tmp %= MOD
        tmp *= gyaku[i+1]
        # tmp %= MOD

        ret += tmp
        ret %= MOD

    return ret

def main():
    r1, c1, r2, c2 = getlist()
    # factorial = [1]
    # tmp = 1
    # t1 = time.time()
    # for i in range(1, r2 + c2 + 5):
    #     tmp *= i
    #     tmp %= MOD
    #     factorial.append(tmp)
    # print(time.time() - t1)
    # gyaku = [pow(i, MOD - 2, MOD) for i in factorial]
    # print(time.time() - t1)
    SIZE = 2 * 10 ** 6 + 10 ** 5
    SIZE += 1
    inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
    fac = [0] * SIZE  # fac[j] = j! mod MOD
    finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    factorial = fac
    gyaku = finv
    # print(time.time() - t1)
    # return
    # gyaku = [1 for i in range(2000000)]
    # print(routes_from_zero(r2, c2))
    # print(routes_from_zero(r1, c2))
    # print(routes_from_zero(r2, c1))
    # print(routes_from_zero(r1, c1))
    ans = routes_from_zero(r2, c2, factorial, gyaku) - routes_from_zero(r1 - 1, c2, factorial, gyaku)\
          - routes_from_zero(r2, c1 - 1, factorial, gyaku) + routes_from_zero(r1 - 1, c1 - 1, factorial, gyaku)
    print(ans % MOD)

if __name__ == '__main__':
    main()
