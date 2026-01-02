from collections import deque


def getPath(adj, start, goal):
    q = deque()
    q.appendleft((start, 0))
    while len(q):
        cur, p = q.pop()
        if cur == goal:
            return p
        for nxt, nhop in adj[cur]:
            if 2**nhop & p:
                continue
            npath = p | 2**nhop
            q.appendleft((nxt, npath))


def bitcount(x):
    return bin(x).count("1")


def main():
    N = int(input())
    adj = [set() for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        adj[a-1].add((b-1, i))
        adj[b-1].add((a-1, i))
    M = int(input())
    dp = [0] * (2**M)
    for i in range(M):
        u, v = map(int, input().split())
        path = getPath(adj, u-1, v-1)
        for j in range(2**i):
            dp[j + 2**i] = dp[j] | path
    ans = 0
    for i in range(2**M):
        ans += (-1) ** bitcount(i) * 2 ** (N - bitcount(dp[i]) - 1)
    print(ans)


if __name__ == "__main__":
    main()
