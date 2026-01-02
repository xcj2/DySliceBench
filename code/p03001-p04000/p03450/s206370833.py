from collections import deque
def bfs(n,fordfs):
    l = [None] * n
    g = fordfs
    for i in range(n):
        if l[i] != None:
            #チェック済みの点iはスキップ
            continue
        l[i] = 0
        que = deque()
        que.append(i)
        while que:
            d = que.pop()
            for node, cost in g[d]:
                if l[node] == None:
                    l[node] = l[d] + cost
                    que.append(node)
                else:
                    if l[node] != l[d] + cost:
                        print('No')
                        exit(0)
    print('Yes')
#    print(l)
    return
##############################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N, M = LI()
g = [[] for _ in range(N)]
for i in range(M):
    x,y,z = map(int,input().split())
#    l = min(x,y)
#    r = max(x,y)
    g[x-1].append((y-1, z))
    g[y-1].append((x-1, -z))

bfs(N,g)