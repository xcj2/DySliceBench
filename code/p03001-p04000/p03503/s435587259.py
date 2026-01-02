import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N = ii()
F = li2(N)
P = li2(N)

B = 2**10

ans = -float('inf')
for i in range(1, B):
    pro = 0
    for j in range(N):
        cnt = 0
        for k in range(11):
            if (i & 1 << k) and F[j][k] == 1:
                cnt += 1
        pro += P[j][cnt]
    ans = max(ans, pro)

print(ans)