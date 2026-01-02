from heapq import heappush, heappop
def dijkstra(adjList, s):
    num = len(adjList)
    dist = [float("INF") for i in range(10)]
    queue = []
    heappush(queue,(0,s))
    dist[s] = 0
    
    while queue != []:
        v_cost, v = heappop(queue)
        if dist[v] < v_cost:
            continue
        for u_cost, u in adjList[v]:
            if u != v and u_cost + dist[v] < dist[u]:
                dist[u] = u_cost + dist[v]
                heappush(queue, (dist[u], u))
    return dist

 
 
from sys import stdin
def IL():return list(map(int, stdin.readline().split()))


h,w = IL()
G = [[] for i in range(10)]
def main(): 
    for i in range(10):
        l = IL()
        for j in range(10):
            G[i].append((l[j],j))
     
     
    ans = 0
    memo={}
    for i in range(h):
        for i in IL():
            if abs(i) == 1:
              pass
            elif i in memo:
              ans += memo[i]
            else:
                t = dijkstra(G, i)[1] 
                memo[i] = t
                ans += t
    print(ans)

if __name__ == "__main__":
    main()