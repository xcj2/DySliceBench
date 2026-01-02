import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

'''
from numpy.linalg import solve

N =ii()
left = dp2(0, N, N)
for i in range(N-1):
    left[i][i] = left[i][i+1] = 0.5
left[N-1][N-1] = left[N-1][0] = 0.5

right = li()

for i in solve(left, right):
    print(int(i), end='')
    print(' ', end='')
'''

N = ii()
A = li()

ans = [0]*N

ans[0] = sum(A) - sum([A[i] for i in range(1, N, 2)])*2
for i in range(N-1):
    ans[i+1] = A[i]*2 - ans[i]

for i in range(N):
    print(ans[i], end='')
    print(' ', end='')