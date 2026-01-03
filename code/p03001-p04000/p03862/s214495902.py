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

N, x = mi()
A = li()
adj = []
'''
for i in range(N-1):
    adj.append(A[i]+A[i+1])

ans = 0
for i, num in enumerate(adj):
    if num > x:
        ans += num - x
        if i < N-2:
            adj[i+1] = max(adj[i+1] - (num-x), A[i+2])
print(ans)
'''
ans = 0
for i in range(N-1):
    if A[i] + A[i+1] > x:
        wa = A[i] + A[i+1]
        ans += wa - x
        if A[i+1] < wa - x:
            A[i+1] = 0
        else:
            A[i+1] -= wa - x

print(ans)