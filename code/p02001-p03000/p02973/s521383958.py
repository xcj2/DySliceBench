def JOI14_B():
    N = I()
    A = [I()for _ in range(N)]
    A.extend(A)
    dp = [[0]*(N*2+1) for _ in range(N*2+1)]

    for j in range(N):
        for i in range(N*2-j):
            if (N-j)%2==1:
                dp[i][i+j] = max(dp[i+1][i+j]+A[i],dp[i][i+j-1]+A[i+j])
            else:
                if A[i]>A[i+j]:
                    dp[i][i+j] = dp[i+1][i+j]
                else:
                    dp[i][i+j] = dp[i][i+j-1]
    ans = 0
    for i in range(N):
        ans = max(ans,dp[i][i+N-1])
    print(ans)
    #print(dp)
    return

def square869120Contest1_G():
    def held_karp(dists,TL):
        # Copyright (c) 2016 Carl Ekerot
        """
        Implementation of Held-Karp, an algorithm that solves the Traveling
        Salesman Problem using dynamic programming with memoization.
        Parameters:
            dists: distance matrix
        Returns:
            A tuple, (cost, path).
        """
        n = len(dists)

        # Maps each subset of the nodes to the cost to reach that subset, as well
        # as what node it passed before reaching this subset.
        # Node subsets are represented as set bits.
        C = {}
        dp = defaultdict(int)

        # Set transition cost from initial state
        for k in range(1, n):
            C[(1 << k, k)] = (dists[0][k], 0)
            dp[(1 << k, k)] = 1

        # Iterate subsets of increasing length and store intermediate results
        # in classic dynamic programming manner
        for subset_size in range(2, n):
            for subset in itertools.combinations(range(1, n), subset_size):
                # Set bits for all nodes in this subset
                bits = 0
                for bit in subset:
                    bits |= 1 << bit
                shortest_length = inf
                # Find the lowest cost to get to this subset
                for k in subset:
                    prev = bits & ~(1 << k)

                    res = []
                    for m in subset:
                        if not (prev, m) in C:
                            continue
                        if m == 0 or m == k:
                            continue
                        if C[(prev, m)][0] + dists[m][k]>TL[m][k]:
                            continue
                        res.append((C[(prev, m)][0] + dists[m][k], m))
                        if shortest_length>C[(prev, m)][0] + dists[m][k]:
                            shortest_length = C[(prev, m)][0] + dists[m][k]
                    if not res:
                        continue
                    C[(bits, k)] = min(res)
                    for d,m in res:
                        if shortest_length!=d:
                            continue
                        dp[(bits, k)] += dp[(prev,m)]

        # We're interested in all bits but the least significant (the start state)
        bits = (2 ** n - 1) - 1

        # Calculate optimal cost
        res = []
        shortest_length = inf
        for k in range(1, n):
            if not (bits, k) in C:
                continue
            if C[(bits, k)][0] + dists[k][0] > TL[k][0]:
                continue
            res.append((C[(bits, k)][0] + dists[k][0], k))
            if shortest_length > C[(bits, k)][0] + dists[k][0]:
                shortest_length = C[(bits, k)][0] + dists[k][0]
        if not res:
            return False
        opt, parent = min(res)
        way = 0
        for d, k in res:
            if not (bits, k) in C:
                continue
            if C[(bits, k)][0] + dists[k][0] > TL[k][0]:
                continue
            if shortest_length < d:
                continue
            way += dp[(bits,k)]

        # Backtrack to find full path
        path = []
        for i in range(n - 1):
            path.append(parent)
            new_bits = bits & ~(1 << parent)
            _, parent = C[(bits, parent)]
            bits = new_bits

        # Add implicit start state
        path.append(0)

        return shortest_length, list(reversed(path)), way

    N, M = LI()
    dist = [[inf]*N for _ in range(N)]
    TL = [[0]*N for _ in range(N)]
    for _ in range(M):
        s, t, d, time = LI()
        s -= 1; t -= 1
        dist[s][t] = dist[t][s] = d
        TL[s][t] = TL[t][s] = time
    ans = held_karp(dist,TL)
    if (not ans) or ans[2]==0:
        print("IMPOSSIBLE")
        return
    print(ans[0],ans[2])
    return

def JOI13_D():
    def solve(yday,leader,next):
        a = [0]*3
        for i in range(3):
            if next&(1<<i)==(1<<i):
                a[i] = 1
        rep = 0
        if a[leader]==0:
            return rep
        for i in range(3):
            if yday&(1<<i)==(1<<i):
                if a[i]==1:
                    rep = 1
        return rep
    N = I()
    S = SI()
    member = {"J":0,"O":1,"I":2}
    dp = [[0]*8 for _ in range(N+1)]
    dp[0][1] = 1
    for i in range(N):
        leader = member[S[i]]
        for j in range(8):
            for k in range(8):
                dp[i+1][j] += (dp[i][k]*solve(k,leader,j))
    ans = sum(dp[-1])%10007
    #print(dp)
    print(ans)
    return

def JOI16_D():
    N, M = LI()
    A = [(I()-1)for _ in range(N)]
    imos = [[0] * (N + 1) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            imos[i][j + 1] += imos[i][j] + (A[j] != i)
    cnt = Counter(A)
    dp = [10 ** 9] * (1 << M)
    num = [None] * (1 << M)
    dp[0] = 0
    num[0] = 0
    for b in range(1 << M):
        for i in range(M):
            if b & (1 << i):
                continue
            nb = b | (1 << i)
            if num[nb] is None:
                num[nb] = num[b] + cnt[i]
            l = num[b]
            r = l + cnt[i]
            d = imos[i][r] - imos[i][l]
            dp[nb] = min(dp[nb], dp[b] + d)

    print(dp[-1])
    return

def ABC6_D():
    N = I()
    C = [I() for _ in range(N)]
    LIS = [C[0]]
    for i in range(N):
        if C[i] > LIS[-1]:
            LIS.append(C[i])
        else:
            LIS[bisect.bisect_left(LIS, C[i])] = C[i]
    print(N - len(LIS))
    return

def ABC134_E():
    N = I()
    A = [I()for _ in range(N)]
    que = deque()
    que.append(A[0])
    L = 1
    for i in range(1,N):
        cur = bisect.bisect_left(que,A[i])
        #print(que,cur,L)
        if cur==0:
            que.appendleft(A[i])
            L += 1
        else:
            que[cur-1] = A[i]

    #print(que)
    ans = len(que)
    print(ans)

    return

def JOI7_F():
    n, k = LI()
    for _ in range(k):
        A = LI()

    return

def square869120Contest1_E():
    N, Q = LI()
    A = LI()
    C = LI()
    C.append(1)
    L = [0]*N
    for i in range(1,N):
        L[i] = pow(A[i-1],A[i],mod) + L[i-1]
    #print(L)
    ans = 0
    now = 0
    for i in range(Q+1):
        next = C[i]-1
        cur = abs(L[next]-L[now])
        ans += cur
        ans %= mod
        now = next
        #print(ans)
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    ABC134_E()
"""

"""