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
import itertools #list(accumulate(A))

S = input()
K = ii()
N = len(S)


alphabets = list('abcdefghijklmnopqrstuvwxyz')
l = []

for alpha in alphabets:
    for i, m in enumerate(S):
        if m == alpha:
            flag = 1
            for j in range(1, min(K+1, N-i+1)):
                l.append(S[i:i+j])
    #print(set(l))
    l = sorted(set(l))
    if len(l) >= K:
        print(l[K-1])
        exit()