import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n = int(input())
es=[[] for i in range(n)]
for i in range(n - 1):
   a, b = map(int, input().split())
   es[a - 1].append(b - 1)
   es[b - 1].append(a - 1)
def dfs0(v, d, p):
    if v == n - 1:
        return d
    for e in es[v]:
        if e != p:
            k = dfs0(e, d + 1, v)
            if k:
                if isinstance(k, int) and k // 2 == d:
                    return v, e
                return k
    return 0

def dfs1(v, p):
    if v == E:
        return 0
    cnt = 1
    for e in es[v]:
        if e != p:
            cnt += dfs1(e, v)
    return cnt

def dfs2(v, p):
    if v == 0:
        return 0
    cnt = 1
    for e in es[v]:
        if e != p:
            cnt += dfs2(e, v)
    return cnt
V, E = dfs0(0, 0, -1)
if  2*dfs1(0, -1) > n:
    print("Fennec")
else:
    print("Snuke")
