INF = 10**9
import sys
from heapq import *
input = sys.stdin.readline

class Dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.dist = [INF] * len(adj)
        self.q = []

    def calc(self, start):
        self.dist[start] = 0
        heappush(self.q, (0, start))
        while len(self.q) != 0:
            prov_cost, src = heappop(self.q)
            if self.dist[src] < prov_cost:
                continue
            for dest, cost in self.adj[src]:
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost
                    heappush(self.q, (self.dist[dest], dest))
        return self.dist

def sep(): return map(int,input().split())
def solve():
    h,w = sep()
    x,y = sep()
    xnot ,ynot = sep()
    x-=1
    y-=1
    xnot-=1
    ynot-=1

    field = []
    for i in range(h):
        temp = input().rstrip()
        field.append(temp)

    edge = [[] for i in range(h*w)]
    for i in range(h):
        for j in range(w):
            if field[i][j] == "#":
                continue
            frm = i * w + j
            for dx in range(-2, 3):
                nx = i + dx
                if nx < 0 or nx > h - 1:
                    continue
                for dy in range(-2, 3):
                    if dx == 0 and dy == 0:
                        continue
                    ny = j + dy
                    if ny < 0 or ny > w - 1:
                        continue
                    if field[nx][ny] == "#":
                        continue
                    dist = abs(dx) + abs(dy)
                    if dist == 1:
                        edge[frm].append((nx*w + ny, 0))
                    else:
                        edge[frm].append((nx*w + ny, 1))


    # for i in range(n):
    #     for j in range(m):
    #         if(grid[i][j] == '#'):
    #             continue
    #         for ii in range(i-2,i+3):
    #             for jj in range(j-2,j+3):
    #                 if(ii==i and jj==j):
    #                     continue
    #                 if(0<=ii<n and 0<=jj<m and grid[ii][jj] == '.'):
    #                     if(abs(ii-i)+abs(jj-j) == 1):
    #                         g[i*m+j].append([ii*m+jj,0])
    #                     else:
    #                         g[i*m+j].append([ii*m+jj,1])
                        # print(i*m+j,ii*m+jj)
    # for i in range(n*m):
    #     print(g[i])

    # dist = [10**9]*(n*m)
    # print(x*m+y,xnot*m+ynot)
    d = Dijkstra(edge)
    dist = d.calc(x*w+y)
    # print(dist[xnot*m+ynot])
    # print(dist)
    if(dist[xnot*w+ynot] == 10**9):
        print(-1)
    else:
        print(dist[xnot*w+ynot])

solve()
