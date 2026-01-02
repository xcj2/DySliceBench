# coding: utf-8
# Your code here!

import queue

INF = 2000000000

class Edge:
    def __init__(self, to, weight, val):
        self.val = val
        self.to = to
        self.weight = weight
        
def bfs(s):
    global d
    d = [INF] * n
    Q.put(s)
    d[s] = 0
    
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            e = G[u][i]
            
            if d[e.to] == INF:
                d[e.to] = d[u] + e.weight
                Q.put(e.to)


def solve():
    bfs(0)
    
    tgt = 0
    maxv = 0
    for i in range(n):
        if d[i] == INF:
            continue
        if maxv < d[i]:
            maxv = d[i]
            tgt = i
    bfs(tgt)
    
    maxv = 0
    for i in range(n):
        if d[i] == INF:
            continue
        if maxv < d[i]:
            maxv = d[i]
    return maxv

n = int(input())

G = [[] for j in range(n)]
d = [INF] * n
for i in range(n-1):
    nums=list(map(int,input().split()))
    G[nums[0]].append(Edge(nums[1], nums[2], i))
    G[nums[1]].append(Edge(nums[0], nums[2], i))
Q = queue.Queue()
print(solve())














