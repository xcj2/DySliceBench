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

## UnionFind

N, M = mi()
memo = []
rel = [[] for i in range(N)]
#d = dp2(float('inf'), N, N)

for i in range(M):
    s, t = mi()
    s, t = s-1, t-1
    memo.append((s, t))
    rel[s].append(t)
    rel[t].append(s)
    #d[s][t] = d[t][s] = 1
#print(d)

def dfs(v):
    #print(v, used)
    for nv in rel[v]:
    #for nv in range(N):
        if not used[nv]:
        #if d[v][nv] != float('inf') and not used[nv]:
            used[nv] = 1
            dfs(nv)
            if sum(used) == N:
                global flag
                flag = True
                return
            #used[nv] = 0

cnt = M
for x in range(M):
    s, t = memo[x][0], memo[x][1]
    rel[s].remove(t)
    rel[t].remove(s)
    #print(rel)
    #print(s, t)
    #d[s][t] = d[t][s] = float('inf')
    #print(d)
    for i in range(N):
        #print(x, i)
        flag = 0
        used = [0]*N
        used[i] = 1
        dfs(i)
        #print(flag)
        if flag:
            cnt -= 1
            break
    rel[s].append(t)
    rel[t].append(s)
    #d[s][t] = d[t][s] = 1

print(cnt)