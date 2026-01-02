import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
XL = li2(N)
R = dp2(0, 2, N)

for i in range(N):
    R[i][0] = XL[i][0] - XL[i][1]
    R[i][1] = XL[i][0] + XL[i][1]


R = sorted(R, key=lambda x:x[1])
m = -float('inf')
cnt = 0
for i in range(N):
    if R[i][0] >= m:
        cnt += 1
        m = R[i][1]

print(cnt)