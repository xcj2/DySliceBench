import sys
import time
input = sys.stdin.buffer.readline
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


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def tasikame(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n + 1):
                tmp = math.gcd(i, j)
                ans += math.gcd(tmp, k)

    return ans


def main():
    n, k = getlist()
    ans = 0
    kumi = [0 for i in range(k+1)]
    for ii in range(k):
        i = k - ii
        cand = k // i
        # 総数　ほう助なし
        tmp = pow(cand, n, MOD)
        # ttmp = i
        # print(tmp)
        # child = make_divisors(i)
        # for ch in child:
        #     kumi[ch] += tmp
        # while(True):
        #     ttmp += i
        #     if ttmp > k:
        #         break
        #     tmp -= kumi[ttmp]
            # print(tmp)
        tmp -= kumi[i]
        child = make_divisors(i)
        for ch in child:
            kumi[ch] += tmp
        # tmp -= (cand - 1) ** n
        ans += (tmp * i) % MOD
        ans %= MOD
        kumi[i] = tmp
        # print(i, ans, tmp, n)
    print(ans)
    # print(tasikame(k))

if __name__ == '__main__':
    main()
