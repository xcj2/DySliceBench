from collections import deque
import sys
input = sys.stdin.readline

def solve():
    MOD = 10**9 + 7

    H, W, N = map(int, input().split())
    rcs = [tuple(map(int, input().split())) for _ in range(N)]

    adjL = [[] for _ in range(N)]
    for i in range(N):
        r1, c1 = rcs[i]
        for j in range(i+1, N):
            r2, c2 = rcs[j]
            if r1 <= r2 and c1 <= c2:
                adjL[i].append(j)
            if r1 >= r2 and c1 >= c2:
                adjL[j].append(i)

    def TopologicalSort(adjList):
        numV = len(adjList)
        indegs = [0] * numV
        for v in range(numV):
            for v2 in adjList[v]:
                indegs[v2] += 1
        anss = [v for v in range(numV) if indegs[v] == 0]
        Q = deque(anss)
        while Q:
            vNow = Q.popleft()
            for v2 in adjList[vNow]:
                indegs[v2] -= 1
                if indegs[v2] == 0:
                    anss.append(v2)
                    Q.append(v2)
        return anss
    nos = TopologicalSort(adjL)

    def getFacts(n, MOD):
        facts = [1] * (n+1)
        for x in range(2, n+1):
            facts[x] = (facts[x-1] * x) % MOD
        return facts
    facts = getFacts(H+W, MOD)
    def getInvFacts(n, MOD):
        invFacts = [0] * (n+1)
        invFacts[n] = pow(facts[n], MOD-2, MOD)
        for x in reversed(range(n)):
            invFacts[x] = (invFacts[x+1] * (x+1)) % MOD
        return invFacts
    invFacts = getInvFacts(H+W, MOD)

    def getNum(r, c, MOD):
        return facts[r+c] * invFacts[r] * invFacts[c] % MOD

    dp = [0] * N
    for i in range(N):
        noi = nos[i]
        r1, c1 = rcs[noi]
        v = getNum(r1-1, c1-1, MOD)
        for j in range(i):
            noj = nos[j]
            r0, c0 = rcs[noj]
            if i == j or r0 > r1 or c0 > c1:
                continue
            dr, dc = r1-r0, c1-c0
            v -= dp[noj] * getNum(dr, dc, MOD)
            v %= MOD
        dp[noi] = v

    ans = getNum(H-1, W-1, MOD)
    for i, (r, c) in enumerate(rcs):
        dr, dc = H-r, W-c
        ans -= dp[i] * getNum(dr, dc, MOD)
        ans %= MOD

    print(ans)


solve()
