def A():
    c = input()
    print(chr(ord(c)+1))

def B():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    K = temp[1]
    M = temp[2]
    A = [int(k) for k in input().split()]
    ans = M*N - sum(A)
    if ans <= K:
        print(max(0, ans))
    else:
        print(-1)

from collections import defaultdict
def C():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    M = temp[1]
    penal = defaultdict(int)
    P = []
    S = []
    for i in range(M):
        temp = input().split()
        P.append(int(temp[0]))
        S.append(temp[1])
    ac_problems = set()

    for i in range(M-1, -1, -1):
        if P[i] not in ac_problems and S[i] == 'AC':
            ac_problems.add(P[i])
        elif P[i] in ac_problems:
            if S[i] == 'WA':
                penal[P[i]] += 1
            elif S[i] == 'AC':
                penal[P[i]] = 0
    
    print(len(ac_problems), sum(penal.values()))

def D():
    temp = [int(k) for k in input().split()]
    H = temp[0]
    W = temp[1]
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def bfs(x, y):
        to_visit = [(x, y, 0)]
        visited = set()
        ret = 0
        while to_visit:
            x, y, distance = to_visit[0]
            del to_visit[0]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            ret = max(distance, ret)
            for d in directions:
                if x+d[0] < H and x+d[0] >= 0:
                    if y+d[1] < W and y+d[1] >= 0:
                        if (x+d[0], y+d[1]) not in visited:
                            if S[x+d[0]][y+d[1]] == '.':
                                to_visit.append((x+d[0], y+d[1], distance+1))
        #print(memo)
        return ret

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(bfs(i, j), ans)
                
    #print(memo)

    print(ans)

def E():
    temp = [int(k) for k in input().split()]
    N = temp[0]
    K = temp[1]
    A = [int(k) for k in input().split()]
    MOD = 10**9+7

    fac = [0]*(N+1)
    fac[0] = fac[1] = 1
    inv = [0]*(N+1)
    inv[1] = 1
    facinv = [0]*(N+1)
    facinv[0] = facinv[1] = 1
    for i in range(2,N+1):
        fac[i] = fac[i-1]*i%MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
        facinv[i] = facinv[i-1] * inv[i] % MOD

    A.sort()

    def nCr(n, r, mod):
        if n < r or n < 0 or r < 0:
            return 0
        else:
            return fac[n] * (facinv[r] * facinv[n-r] % mod) % mod

    maximum_sum = 0
    minimum_sum = 0
    for i in range(N):
        maximum_sum += nCr(i, K-1, MOD)*A[i]
        maximum_sum %= MOD
        minimum_sum += nCr(N-i-1, K-1, MOD)*A[i]
        minimum_sum %= MOD

    print((maximum_sum-minimum_sum)%MOD)


E()