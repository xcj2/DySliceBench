import sys
import heapq as h

inf = sys.maxsize

class heapq:
    def __init__(self):
        self.q = []

    def push(self,v):
        h.heappush(self.q, v)
    
    def pop(self):
        return h.heappop(self.q)

    def is_empty(self):
        return len(self.q) == 0

# 入力:graphと始点s
# 出力:始点sから各頂点tへの距離dist
def shortestPath0(graph, s):
    n = len(graph)

    dist    = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[s] = 0

    while True:
        idx, u  = -1, inf
        for i in range(n):
            if not visited[i] and dist[i] < u:
                idx = i
                u = dist[i]
        
        if u == inf: break
        
        visited[idx] = True

        for (next, w) in graph[idx]:
            newdist = w + dist[idx]
            if newdist < dist[next]:
                dist[next] = newdist
    return dist

def shortestPath1(graph, s):
    n = len(graph)

    dist    = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    
    q = heapq()
    q.push((0, s))

    while not q.is_empty():
        (cur_dist, v) = q.pop()

        if visited[v] or dist[v] <= cur_dist:
            continue

        dist[v] = cur_dist
        visited[v] = True

        for next, w in graph[v]:
            if not visited[next] and dist[v] + w < dist[next]:
                q.push((dist[v] + w, next))

    return dist

def main():
    v, e, s = map(int, input().split())
    
    # 隣接リスト
    graph = [[] for _ in range(v)]
    
    for i in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
            
    c_dist = shortestPath1(graph, s)
            
    for d in c_dist:
        if d == inf:
            print("INF")
        else:
            print(d)
main()