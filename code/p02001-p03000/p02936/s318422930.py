import sys
sys.setrecursionlimit(200010)
def input():
    return sys.stdin.readline()[:-1]
def main():
    N, Q = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    V = [0]*N
    for _ in range(Q):
        p, x = map(int,input().split())
        V[p-1] += x

    def dfs(mae,ima):
        for tsugi in G[ima]:
            if tsugi != mae:
                V[tsugi] += V[ima]
                dfs(ima,tsugi)
    dfs(-1,0)
    print(*V)

if __name__ == '__main__':
    main()
