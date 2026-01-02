from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)

mod = 10**9 + 7
queue = deque()
queue.append(0)
parent = [-1]*n
parent[0] = 0
while queue:
    now = queue.popleft()
    for to in G[now]:
        if parent[to] == -1:
            parent[to] = now
            queue.append(to)

data1 = [[0,0] for i in range(n)]
def factorial(N,MOD,r=True):
    fact = [1]*(N+1)
    rfact = [1]*(N+1)
    r = 1
    for i in range(1,N+1):
        fact[i] = r = r * i % MOD
    rfact[N] = r = pow(fact[N],MOD-2,MOD)
    for i in range(N, 0, -1):
        rfact[i-1] = r = r * i % MOD
    if r:
        return fact,rfact
    else:
        return fact

fact,rfact = factorial(2*10**5,mod)
def com(l):
    res = 1
    s = 0
    for x in l:
        res *= rfact[x]
        res %= mod
        s += x
    res *= fact[s]
    res %= mod
    return res
def dfs(now,pre):
    if data1[now] != [0,0]:
        return
    if len(G[now]) == 1 and G[now][0] == pre:
        data1[now] = [1,1]
        return
    x,y = 0,1
    child = []
    for to in G[now]:
        if pre == to:
            continue
        dfs(to,now)
        child.append(data1[to][1])
        y *= data1[to][0]
        y %= mod
    res = y * com(child)
    res %= mod
    data1[now] = [res,sum(child)+1]
    return

dfs(0,-1)

ans = [data1[i][0] for i in range(n)]

que = deque()
que.append([0,0])
while que:
    now,pre = que.popleft()
    for to in G[now]:
        if to == pre:continue
        ans[to] = ans[now]*data1[to][1]*pow(n-data1[to][1],mod-2,mod)
        ans[to] %= mod
        que.append([to,now])

for x in ans:
    print(x)