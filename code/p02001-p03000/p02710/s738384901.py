mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    def calc(n):
        return (n * (n-1)) // 2 + n

    def merge(A, B):
        if len(A) > len(B):
            A, B = B, A
        for a in A:
            if a in B:
                B[a] += A[a]
            else:
                B[a] = A[a]
        return B

    N = int(input())
    C = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    que = deque()
    que.append(1)
    seen = [-1] * (N+1)
    seen[1] = 0
    par = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    seq = []
    while que:
        v = que.popleft()
        seq.append(v)
        for u in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + 1
                par[u] = v
                child[v].append(u)
                que.append(u)
    seq.reverse()

    size = [1] * (N+1)
    dic = [{} for _ in range(N+1)]
    ans = [calc(N)] * (N+1)
    for v in seq:
        for u in child[v]:
            size[v] += size[u]
        c = C[v-1]
        for u in child[v]:
            if c in dic[u]:
                ans[c] -= calc(size[u] - dic[u][c])
            else:
                ans[c] -= calc(size[u])
            dic[v] = merge(dic[v], dic[u])
        dic[v][c] = size[v]
    for c in range(1, N+1):
        if c in dic[1]:
            print(ans[c] - calc(N - dic[1][c]))
        else:
            print(ans[c] - calc(N))


if __name__ == '__main__':
    main()
