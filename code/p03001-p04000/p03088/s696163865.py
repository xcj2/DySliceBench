import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def solve():
    n = getN()
    dp = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Free(C/T), A, G, AG, AC, AT, GA, AGA, AGG, AGT, ATG, (OUT)
    #     0      1  2   3   4   5   6   7    8    9    10

    for i in range(n):
        tmp = [0] * 12

        tmp[3] = dp[1] + dp[6] + dp[7]
        tmp[4] = dp[1]
        tmp[5] = dp[1] + dp[6] + dp[7]
        tmp[6] = dp[2] + dp[8] + dp[10]
        tmp[7] = dp[3]
        tmp[8] = dp[3]
        tmp[9] = dp[3]
        tmp[10] = dp[5]
        tmp[11] = dp[3] + dp[4] + dp[6] + dp[7] + dp[8] + dp[9] + dp[10] + dp[11] * 4
        tmp[1] = dp[0] + dp[1] + dp[4] + dp[5] + dp[6] + dp[7] + dp[9]
        tmp[2] = dp[0] + dp[2] + dp[8] + dp[9] + dp[10]
        tmp[0] = dp[0] * 2 + dp[2] * 2 + dp[4] * 2 + dp[5] * 2 + dp[8] + dp[9] + dp[10]

        dp = [x % MOD for x in tmp]
    #     print(dp)
    # print(sum(dp)%MOD)
    # print(pow(4, n, MOD))
    print(sum(dp[:-1]) % MOD)

def gu(n=5):
    ban = ["AGC", "ACG", "GAC", "AGAC", "AGGC", "AGTC", "ATGC"]
    select = ["A", "G", "C", "T"]
    ans = 0
    space = [0] * 11
    sp = ["ATG", "AGT", "AGG", "AGA", "GA", "AT", "AC", "AG", "G", "A"]
    for i in range(4 ** n):
        lis = []
        for j in range(n):
            lis.append(select[i%4])
            i //= 4
        ji = "".join(lis)
        fl = True
        # print(ji)
        for b in ban:
            if b in ji:
                fl = False
        if fl:
            ans += 1
            en = False
            for dd, spp in enumerate(sp):
                if ji.endswith(spp):
                    space[dd] += 1
                    en = True
                    break
            if not en:
                space[-1] += 1

    space.reverse()

    print(space)
    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()
    # for i in range(1, 7):
    #     gu(i)




