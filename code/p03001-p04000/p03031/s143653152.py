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

N, M = mi()
ks = []
for i in range(M):
    a = li()
    ks.append(a)
P = li()

cnt = 0
pattern = [0]*N

def dfs(pattern, pos):
    if pos == N:
        for i in range(M):
            num , *switches = ks[i]
            if sum([pattern[sw-1] for sw in switches]) % 2 != P[i]:
                break
        else:
            global cnt
            cnt += 1
    else:
        pattern[pos] = 0
        dfs(pattern, pos+1)
        pattern[pos] = 1
        dfs(pattern, pos+1)
        
dfs(pattern, 0)
print(cnt)