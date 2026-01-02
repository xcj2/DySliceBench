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


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = S()
    K = I()
    dig = len(N)
    if dig < K:
        print(0)
        exit()
    ans = 0
    for i in range(dig):
        if K == 0:
            ans += 1
            break
        if int(N[i]) == 0:
            continue
        if dig - i - 1 >= K:
            ans += combinations_count(dig - i - 1, K) * pow(9, K)
        if dig - i - 1 >= K - 1:
            ans += (int(N[i]) - 1) * combinations_count(dig - i - 1, K - 1) * pow(9, K - 1)
        if i == dig - 1:
            ans += 1
        K -= 1
    print(ans)
if __name__ == "__main__":
    main()

