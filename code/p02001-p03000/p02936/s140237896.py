import sys
sys.setrecursionlimit(200010)

def main():
    def input():
        return sys.stdin.readline()[:-1]

    N, Q = map(int,input().split())
    G = [[] for k in range(N)]


    for k in range(N-1):
        a, b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    ans = [0 for k in range(N)]
    for k in range(Q):
        p, x = map(int,input().split())
        ans[p-1] += x

    V = [0 for k in range(N)]
    V[0] = 1
    def dfs(ima):
        for tsugi in G[ima]:
            if V[tsugi] == 0:
                V[tsugi] = 1
                ans[tsugi] += ans[ima]
                dfs(tsugi)
    dfs(0)

    print(*ans,sep=" ")

if __name__ == '__main__':
    main()
