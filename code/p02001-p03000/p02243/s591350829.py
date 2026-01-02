import sys

f_i = sys.stdin

n = int(f_i.readline())

class VCost:
    def __init__(self, v, cost):
        self.v_n = v
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
    def __gt__(self, other):
        return self.cost > other.cost

adj = [[VCost(int(v), int(c)) for v, c in zip(x.split()[2::2], x.split()[3::2])] for x in f_i]

import heapq

def dijkstra():
    PQ = []
    isVisited = [False] * n
    distance = [999900001] * n

    distance[0] = 0
    heapq.heappush(PQ, VCost(0, 0))
    
    while PQ:
        uc = heapq.heappop(PQ)
        u = uc.v_n

        if uc.cost > distance[uc.v_n]:
            continue

        isVisited[u] = True
        
        for vc in adj[u]:
            v = vc.v_n
            if isVisited[v] == True:
                continue
            t_cost = distance[u] + vc.cost
            if t_cost < distance[v]:
                distance[v] = t_cost
                heapq.heappush(PQ, VCost(v, t_cost))

    for v, d in enumerate(distance):
        print(v, d)


dijkstra()