import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N = ii()
S = [input() for _ in range(N)]
d = defaultdict()
d[S[0]] = 1
for i in range(1, N):
    if S[i] in d.keys():
        print('No')
        exit()
    d[S[i]] = 1
    if S[i][0] != S[i-1][-1]:
        print('No')
        exit()
print('Yes')