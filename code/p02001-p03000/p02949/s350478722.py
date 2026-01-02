import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,m,p=map(int,input().split())
g=[[] for _ in range(n)]
g2=[[] for _ in range(n)]
g3=[[] for _ in range(n)]
for _ in range(m):
    a,b,l=map(int,input().split())
    g[a-1].append([b-1,p-l])
    g2[a-1].append(b-1)
    g3[b-1].append(a-1)

f1=[False for _ in range(n)]
def dfs1(s):
    global f1
    global g2
    f1[s] = True
    for sg in g2[s]:
        if not f1[sg]:
            dfs1(sg)
f2=[False for _ in range(n)]
def dfs2(s):
    global f2
    global g3
    f2[s] = True
    for sg in g3[s]:
        if not f2[sg]:
            dfs2(sg)

dfs1(0)
dfs2(n-1)
f3 = []
for i in range(n):
    f3.append(f1[i] and f2[i])

def bellman_ford(g,n):
    INF = 10**10
    res = [INF for _ in range(n)]
    res[0] = 0
    for _ in range(n-1):
        for i in range(n):
            if res[i] != INF:
                for sa,sb in g[i]:
                    res[sa] = min(res[sa],res[i]+sb)
    ret = res[-1]
    for i in range(n):
        if res[i] != INF:
            for sa,sb in g[i]:
                if res[sa]>res[i]+sb:
                    if f3[sa]:
                        return False
    return ret

res = bellman_ford(g,n)
if type(res) == bool:
    print(-1)
elif res > 0:
    print(0)
else:
    print(res * -1)