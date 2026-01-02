def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
input = sys.stdin.readline

N,M = Ints()

from collections import defaultdict
Graph = defaultdict(list)

for i in range(M):     #ABC = [now, to, cost] のリストを想定
    A,B = Ints()
    Graph[A].append([B,1])
    Graph[B].append([A,1])

def dijkstra_heap(s,Graph,N):
    import heapq
    que = []
    INF = 10**18
    MIN = [INF]*(N+1)    #N: 頂点数, 1,Nの場合も考慮してる
    From = [-1]*(N+1)
    
    heapq.heappush(que,[0,s])

    while que != []:
        nowc,to = heapq.heappop(que)
        MIN[to] = min(nowc, MIN[to])
        if MIN[to] >= nowc:
            for (b,c) in Graph[to]:
                if nowc+c < MIN[b]:
                    From[b] = to
                    MIN[b] = nowc+c
                    heapq.heappush(que,[nowc+c,b])
    return MIN,From

MIN,From = dijkstra_heap(1,Graph,N+1)

print('Yes')
for i in range(N-1):
    print(From[i+2])