import sys
sys.setrecursionlimit(10**7)
n,m,p = map(int,input().split())
E1 = [[] for i in range(n)]
E2 = [[] for i in range(n)]
edge = []
for i in range(m):
    a,b,c = map(int,input().split())
    c = p-c
    a -= 1
    b -= 1
    E1[a].append(b)
    E2[b].append(a)
    edge.append((a,b,c))

dis1 = [False]*n
def dfs1(x):
    if dis1[x] == False:
        dis1[x] = True
        for nex in E1[x]:
            dfs1(nex)

dis2 = [False]*n
def dfs2(x):
    if dis2[x] == False:
        dis2[x] = True
        for nex in E2[x]:
            dfs2(nex)

dfs1(0)
dfs2(n-1)

ok = []
for i in  range(n):
    if dis1[i] and dis2[i]:
        ok.append(True)
    else:
        ok.append(False)
nedge = []
for a,b,c in edge:
    if ok[a] and ok[b]:
        nedge.append((a,b,c))

def belw():
    dis = [float("INF")]*n
    dis[0] = 0
    count = 0
    check = True

    while check:
        check = False
        for a,b,c in nedge:
            
            if dis[a] != float("INF") and dis[b] > dis[a]+c:
                check = True
                dis[b] = dis[a]+c
        count += 1

        if count > n+1 and check:
            return float("INF")
    
    return -dis[-1]

ans = belw()
if ans == float("INF"):
    print(-1)
else:
    print(max(ans,0))









