import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
from itertools import accumulate #list(accumulate(A))

N = ii()
S = [sorted(li()) for _ in range(3)]
rec = [[0]*N for i in range(3)]

for i in range(N):
    #for j in range(2):
    #rec[0][i] = bisect.bisect_right(S[1], S[0][i])
    rec[1][i] = N - bisect.bisect_right(S[2], S[1][i])

acc = list(accumulate(rec[1]))
#acc_1 = [0] * N
#for i in range(N):
    #ind = bisect.bisect_right(S[2], acc_

ans = 0
for i in range(N):
    #for j in range(rec[0][i], N):
    ind = bisect.bisect_right(S[1], S[0][i])
    if ind == 0:
        ans += acc[-1]
    else:
        ans += acc[-1] - acc[ind-1]

print(ans)