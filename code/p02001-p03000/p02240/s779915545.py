n, m = map(int, input().split())

adj = [[] for i in range(n)]

for i in range(m):
    s, t = map(int, input().split())
    adj[s].append(t)
    adj[t].append(s)

isVisited = [False] * n

CC = [None] * n


def dfs(u, group):
    path = []
    path.append(u)
    isVisited[u] = True
    CC[u] = group
    while path:
        u = path[-1]
        if adj[u]:
            v = adj[u].pop(0)
            if not isVisited[v]:
                isVisited[v] = True
                CC[v] = group
                path.append(v)
        else:
            path.pop()

def makeCC(group):
    for i in range(n):
        if not isVisited[i]:
            dfs(i, group)
            group += 1

def isConnected(v1, v2):
    if CC[v1] == CC[v2]:
        print('yes')
    else:
        print('no')


makeCC(0)


q = int(input())

for i in range(q):
    s, t = map(int, input().split())
    isConnected(s, t)