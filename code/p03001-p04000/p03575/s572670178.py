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
import copy
N, M = mi()
D = dp2(float('inf'), N, N)
memo = []
cnt = 0

for i in range(M):
    s, t = mi()
    s, t = s-1, t-1
    memo.append((s, t))
    D[s][t] = D[t][s] = 1

for x in range(M):
    d = copy.deepcopy(D)
    s, t = memo[x][0], memo[x][1]
    d[s][t] = d[t][s] = float('inf')
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    for i in range(N):
        for j in range(i+1, N):
            if d[i][j] == float('inf'):
                cnt += 1
                break
        else:
            continue
        break

print(cnt)