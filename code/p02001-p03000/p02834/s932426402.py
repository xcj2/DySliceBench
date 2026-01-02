import sys
from collections import deque, defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    N, u, v = map(int, input().split())
    u -= 1
    v -= 1
    
    edges = [map(int, input().split()) for _ in range(N-1)]

    to = [[] for _ in range(N)]
    for a, b in edges:
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)
    
    dist  = {key:defaultdict(int) for key in [u, v]}

    def bfs(key):
        q = deque()
        q.append(key)
        while(len(q)):
            now = q.popleft()
            for nv in to[now]:
                if nv == key or dist[key][nv]:
                    continue
                else:
                    dist[key][nv] = dist[key][now] + 1
                    q.append(nv)
    
    for key in [u, v]:
        bfs(key)
    
    ans = 0
    for i in range(N):
        diff = dist[v][i] - dist[u][i]
        if diff > 0:
            ans = max(ans, dist[v][i]-1)

    print(ans)    

if __name__ == "__main__":
    main()