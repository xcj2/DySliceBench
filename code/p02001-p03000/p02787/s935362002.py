import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
from functools import reduce

def main():
    H, N = MI()
    A = []
    B = []
    A_B = []
    for i in range(N):
        a, b = MI()
        A.append(a)
        B.append(b)
    max_A = max(A)
    #dp[i]=体力iを削るのに必要な最小魔力
    dp = [10 ** 9] * (H + max_A)
    dp[0] = 0
    for j in range(N):
        a_j = A[j]
        b_j = B[j]
        for i in range(H + max_A):
            if i - a_j >= 0:
                dp[i] = min(dp[i - a_j] + b_j, dp[i])
            else:
                dp[i] = min(b_j, dp[i])

    ans = min(dp[H:H + max_A])
    print(ans)


if __name__ == "__main__":
    main()
