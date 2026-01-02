import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**6)
N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
ans = [0] * N

def dfs(v, p):
    for u in tree[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v)

def main():

    for _ in range(N-1):
        a, b = map(int,input().split())
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)

    for _ in range(Q):
        p,x = map(int, input().split())
        ans[p-1] += x
    # print(ans)

    dfs(0, -1)
    print(*ans)

if __name__ == "__main__":
    main()
