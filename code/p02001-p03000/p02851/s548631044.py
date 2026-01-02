import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, K = LI()
    A = LI()
    cumsum = [0] * (N+1)
    c = collections.defaultdict(list)
    memo = [0] * (N+1)
    c[0].append(0)
    for i in range(N):
        # cumsum[i] ... [0, i)
        cumsum[i+1] = (cumsum[i] % K + A[i]) % K
        val = (cumsum[i+1] - (i+1)) % K
        memo[i+1] = val
        c[val].append(i+1)
    # print(cumsum)
    # print(memo)
    # print(c)
    ans = 0
    for i in range(N+1):
        val = memo[i]
        l_ix = bisect.bisect_right(c[val], i)
        r_ix = bisect.bisect_right(c[val], i + (K-1))
        # print('i: {}, memo[i]: {}, c[val]: {}, l_ix: {}, r_ix: {}'.format(i, memo[i], c[val], l_ix, r_ix))
        ans += r_ix - l_ix
    # for i in range(N):
    #     if A[i] % K == 1:
    #         ans += 1
    print(ans)
main()

