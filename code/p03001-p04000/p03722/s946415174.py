#!python3

def mii():
    return map(int, input().split())

from heapq import heappush, heappop

def resolve():
    N, M = mii()
    ab = [[] for i in range(N)]
    for i in range(M):
        a, b, c = mii()
        ab[a-1].append((b-1, c))

    used = [False] * N
    q = [(0, set())]
    while q:
        p1, s1 = q.pop()

        for p2, x in ab[p1]:
            if p2 in s1:
                print("inf")
                return

            s2 = set(s1)
            s2.add(p2)
            q.append((p2, s2))

    q = []
    heappush(q, (0, 0))
    dp = [10**9*N+1] * N
    while q:
        t1, p1 = heappop(q)

        for p2, t2 in ab[p1]:
            t3 = t1 - t2
            if t3 < dp[p2]:
                dp[p2] = t3
                heappush(q, (t3, p2))

    print(-dp[-1])

def resolve():
    N, M = mii()
    ab = [[] for i in range(N)]
    for i in range(M):
        a, b, c = mii()
        ab[a-1].append((b-1, c))


    INF = 10**9*N + 1
    dp = [-INF] * N
    dp[0] = 0
    for i in range(N + 1):
        updated = False
        for p1 in range(N):
            if dp[p1] == -INF: continue

            for p2, t2 in ab[p1]:
                t3 = dp[p1] + t2
                if t3 > dp[p2]:
                    dp[p2] = t3

                    updated = True
        if i == N-1:
            dp0 = dp[-1]
        elif i == N:
            dp1 = dp[-1]
            if dp0 == dp1:
                print(dp1)
            else:
                print("inf")

        if not updated:
            print(dp[-1])
            return



if __name__ == "__main__":
    resolve()
