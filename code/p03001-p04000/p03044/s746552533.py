import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
from collections import deque
#======================================================#
def main():
    n = II()
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        u,v,w = MII()
        graph[u-1].append((w, v-1))
        graph[v-1].append((w, u-1))
    dq = deque()
    color = [-1]*n
    dist = [-1]*n
    dq.append((0,0))
    color[0] = 0
    dist[0] = 0
    while dq:
        prev_cost, src = dq.popleft()
        for cost, dst in graph[src]:
            if dist[dst] != -1:
                continue
            if prev_cost%2 == cost%2:
                color[dst] = 0
            else:
                color[dst] = 1
            dist[dst] = dist[src] + cost
            dq.append((dist[dst], dst))
    print(*color, sep='\n')

if __name__ == '__main__':
    main()