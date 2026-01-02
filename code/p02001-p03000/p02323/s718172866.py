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

## 4/25

V, E = mi()
rel = [[] for _ in range(V)]
inv_rel = [[] for _ in range(V)]
for i in range(E):
    s, t, c = mi()
    rel[s].append((t, c))
    #inv_rel[t].append((s, c))

B = 2**V
dp = dp2(-1, V, B)

# 前向きメモ化再帰
def rec_for(state, now):
    if dp[state][now] != -1:
        return dp[state][now]
    if state == B-1:
        dp[state][now] = 0
        return 0
    res = float('inf')
    for v, c in rel[now]:
        if v==0 and state|(1<<v)!=B-1:
            continue
        if not state & (1<<v):
            res = min(res, rec_for(state|(1<<v), v)+c)
    dp[state][now] = res
    return res

# 後ろ向きメモ化再帰
def rec_back(state, now):
    if dp[state][now] != -1:
        return dp[state][now]
    if state==now==0:
        dp[state][now] = 0
        return 0
    res = float('inf')
    for pv, c in inv_rel[now]:
        if pv==0 and state!=1:
            continue
        if state & (1<<pv):
            res = min(res, rec_back(state^(1<<pv), pv)+c)
    dp[state][now] = res
    return res

ans = rec_for(0, 0)
#ans = rec_back(B-1, 0)
if ans == float('inf'):
    print(-1)
    exit()
print(ans)

'''
# DP
dp = dp2(float('inf'), V, B)
dp[0][0] = 0

for state in range(B-1):
    for now in range(V):
        if dp[state][now] != float('inf'):
            for nv, c in rel[now]:
                #if nv == 0 and state|1 != B-1:
                    #continue
                if not state & 1<<nv:
                    dp[state|(1<<nv)][nv] = min(dp[state|(1<<nv)][nv], dp[state][now]+c)

if dp[B-1][0] == float('inf'):
    print(-1)
    exit()
print(dp[B-1][0])
'''
