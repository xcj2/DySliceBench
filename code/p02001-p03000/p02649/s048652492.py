import sys
readline = sys.stdin.readline

def popcount(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

Jm = 18

MOD = 10**18+3
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
frac, fraci = frac(100)
def comb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a]*fraci[b]*fraci[a-b]%MOD


PP = (1<<32) - 1
def popcount64(x):
    return popcount(PP&x) + popcount(x>>32)



N, K, S, T = map(int, readline().split())
lim = 60
calc = [0]*lim
for n in range(lim):
    for j in range(K):
        calc[n] += comb(n, j)

A = list(map(int, readline().split()))

ans = 1
table = [-1]*Jm
for i in range(Jm):
    si = S&(1<<i)
    ti = T&(1<<i)
    if si and ti:
        table[i] = 1
        continue
    if si and not ti:
        ans = 0
        break
    if not si and not ti:
        table[i] = 0
        continue        


if not ans:
    print(ans)
else:
    ans = 0
    B = []
    for idx in range(N):
        for i in range(Jm):
            if table[i] == 1:
                if not (A[idx] & (1<<i)):
                    break
            if table[i] == 0:
                if (A[idx] & (1<<i)):
                    break
        else:
            res = 0
            cnt = -1
            ctr = 0
            for i in range(Jm):
                if table[i] == -1:
                    ctr += 1
                    cnt += 1
                    if A[idx] & (1<<i):
                        res |= (1<<cnt)
            B.append(res)
    
    Jm = ctr
    L = len(B)
    JJ = (1<<L)-1

    G = [[0]*L for _ in range(Jm)]
    for i in range(Jm):
        for idx in range(L):
            res = 0
            for jdx in range(idx+1, L):
                if (1<<i) & B[idx] == (1<<i) & B[jdx]:
                    res |= 1<<jdx
            G[i][idx] = res
    
    
    H = [[0]*L for _ in range(1<<Jm)]
    for i in range(L):
        H[0][i] = JJ
    
    ans = 0
    for k in range(1, K+1):
        ans += comb(L, k)
    #print(B, ans)
    for U in range(1, 1<<Jm):
        R = []
        res = 0
        K = -U&U
        Uk = U^K
        for idx in range(L):
            H[U][idx] = H[Uk][idx] & G[K.bit_length()-1][idx]
            cnt = H[U][idx]
            res += calc[popcount64(cnt)]
        #print(U, (-1 if len(R)&1 else 1)*res)
        ans += (-1 if popcount(U)&1 else 1)*res
    print(ans)
        