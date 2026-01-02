import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def era(n):
    ret = [1 for i in range(n + 2)]
    for i in range(2, int(math.sqrt(n) +3)):
        if ret[i] != 0:
            for j in range(2, n//i + 1):
                ret[i * j] = 0
    rret = []
    for i, r in enumerate(ret):
        if r == 1 and i != 0:
            rret.append(i)

    return rret


def houjyo(n, m, k, kaijyo):
    # kaburi ... k
    # all ... n
    if k == n:
        return 1
    else:
        # kasanarierabi nck * nokorierabi (m - k)p(n-k) - houjyo(+1)
        ret = nck(n,k,kaijyo) * npk(m-k, n-k, kaijyo) # - (k + 1) * houjyo(n, m, k+1, kaijyo)
        # print(nck(n,k,kaijyo) , npk(m-k, n-k, kaijyo))
        return ret % MOD


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret


def solve():
    n = getN()
    nums = getList()

    ref = [0,0,0]
    ans = 1
    for num in nums:
        tmp = num
        ref.sort()
        if ref[0] == tmp:
            if ref[0] == ref[1]:
                if ref[0] == ref[2]:
                    ans *= 3
                else:
                    ans *= 2
            ref[0] += 1

        elif ref[1] == tmp:
            if ref[1] == ref[2]:
                ans *= 2

            ref[1] += 1
        elif ref[2] == tmp:
            ref[2] += 1
        else:
            print(0)
            return
        ans %= MOD
        # print(ans)

    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()