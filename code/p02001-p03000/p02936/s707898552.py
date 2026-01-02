import sys, math
sys.setrecursionlimit(200010)

def input():
    return sys.stdin.readline()[:-1]

def main():
    N, Q = map(int,input().split())
    G = [[] for k in range(N)]
    for k in range(N-1):
        a, b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    V = [0]*N
    D = [0]*N
    for k in range(Q):
        p, x = map(int,input().split())
        D[p-1] += x

    def dfs(visited,distance,graph,ima):
        for e in graph[ima]:
            if visited[e] == 0:
                visited[e] = 1
                distance[e] += distance[ima]
                dfs(visited,distance,graph,e)
    V[0] = 1
    dfs(V,D,G,0)

    print(*D)

if __name__ == '__main__':
    main()
