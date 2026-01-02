# ----------- gcd ----------- #
def gcd(x, y):
    k, l = x, y
    if y < 0:
        k, l = -k, -l
    while l:
        k, l = l, k % l
    return k
def extgcd(a, b, c):
    if b == 0:
        return c // a, 0
    if b < 0:
        a, b, c = -a, -b, -c
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l != 0:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    return c * x, c * y

# --------- IsPrime --------- #
def IsPrime(n):
    if n == 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

# --- fraction calculator --- #
def fracsum(f1, f2, sign = 1):
    fs = [f1[0]*f2[1]+sign*f1[1]*f2[0], f1[1]*f2[1]]
    g = gcd(fs[0], fs[1])
    fs[0] //= g
    fs[1] //= g
    return fs
def fracprod(f1, f2):
    fs = [f1[0]*f2[0], f1[1]*f2[1]]
    g = gcd(fs[0], fs[1])
    fs[0] //= g
    fs[1] //= g
    return fs

# ------ factorization ------ #
def factorization(n):
    D = {}
    a = n
    p = 2
    while a != 1:
        cnt = 0
        while a % p == 0:
            cnt += 1
            a //= p
        if cnt != 0:
            D[p] = cnt
        p += 1
        if p * p > n and a != 1:
            D[a] = 1
            break
    return D
# --------------fact. calculator-------------- #
mod = 0 # <-- input modulo
maxf = 0           # <-- input factional limitation

def doubling(n, m, modulo=0):
    y = 1
    base = n
    tmp = m
    while tmp:
        if tmp % 2 == 1:
            y *= base
            if modulo > 0:
                y %= modulo
        base *= base
        if modulo > 0:
            base %= modulo
        tmp //= 2
    return y
def Vanilla(D):
    F = [1]
    for i in D:
        mL = F[:]
        dp = i
        for j in range(D[i]):
            for k in mL:
                F.append(dp*k)
            dp *= i
    return F
def bic(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt

def inved(a, modulo=5):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l != 0:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    return x % modulo
"""D = {i: [] for i in range(27, 33)}
for i in range(27, 33):
    j = 1
    bas = 2**i
    while len(D[i]) < 5:
        if IsPrime(j*bas+1):
            D[i].append(j*bas+1)
        j += 2
print(D)"""
#mod = 40961
#mod = 998244353, primod = 50475, invmod = 305218526
mod = [2013265921, 2281701377, 3892314113] # 998244353 = 2^23 * (odd number)
primod = [137, 551, 499]
"""for k in range(3):
    S = factorization(mod[k] - 1)
    S = {2: S[2]}
    LL = Vanilla(S)
    print(LL)
    LL.sort(reverse=True)
    for i in range(350, 700):
        flg = (doubling(i, doubling(2, S[2]), mod[k]) == 1)
        for j in range(1, len(LL)):
            flg *= (doubling(i, LL[j], mod[k]) != 1)
        if flg:
            print(mod[k], i)
    print()"""
def powlimit(n):
    y = 1
    cnt = 0
    while y < n:
        y *= 2
        cnt += 1
    return y, cnt

N, M = map(int, input().split())
A = list(map(int, input().split()))
#A = [1 for i in range(N)]
mm = max(A)
F = [0 for _ in range(mm+1)]
for i in range(N):
    F[A[i]] += 1
"""N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
F = [0] + [AB[i][0] for i in range(N)]
G = [0] + [AB[i][1] for i in range(N)]"""
pl, c = powlimit(2*mm+2)
#pl, c = powlimit(2*N+2)
F = F[:] + [0]*(pl-mm-1)
prim = [[doubling(primod[j], doubling(2, 27-i), mod[j]) for i in range(27)] for j in range(2)]
invp = [[inved(prim[j][i], mod[j]) for i in range(27)] for j in range(2)]
#print(prim)
#print(invp)
def NTT(f, n, cn, num, inverse=False):
    if n == 1:
        return f
    if n == 2:
        return [(f[0]+f[1])%mod[num], (f[0]-f[1])%mod[num]]
    dn = n // 2
    fe = [f[2*i+0] for i in range(dn)]
    fo = [f[2*i+1] for i in range(dn)]
    fe = NTT(fe, dn, cn-1, num, inverse)
    fo = NTT(fo, dn, cn-1, num, inverse)
    seed = inverse * prim[num][cn] + (1 - inverse) * invp[num][cn]
    grow = 1
    xf = [0 for _ in range(n)]
    for i in range(dn):
        right = fo[i] * grow % mod[num]
        xf[i+0*dn] = (fe[i] + right) % mod[num]
        xf[i+1*dn] = (fe[i] - right) % mod[num]
        grow *= seed
        grow %= mod[num]
    return xf

X = [NTT(F, pl, c, j) for j in range(2)]
#Y = NTT(G, pl, c)
#print(X)
#print(Y)
Z = [[X[j][i]*X[j][i]%mod[j] for i in range(pl)] for j in range(2)]
for j in range(2):
    Z[j] = NTT(Z[j], pl, c, j, 1)
#print(NTT(Z, pl, c, 1))
W = [0 for _ in range(2*mm+1)]
for j in range(2):
    ipl = inved(pl, mod[j])
    for i in range(pl):
        Z[j][i] *= ipl
        Z[j][i] %= mod[j]
for i in range(2*mm+1):
    k1, k2 = extgcd(mod[0], -mod[1], Z[1][i] - Z[0][i])
    W[i] = (mod[0]*k1+Z[0][i]) % (mod[0]*mod[1])
#print(W)
S = 2*max(A)
hp = 0
ccnt = 0
while ccnt < M:
    if ccnt + W[S] < M:
        ccnt += W[S]
        hp += S * W[S]
    else:
        hp += S * (M - ccnt)
        ccnt += M - ccnt
    S -= 1
print(hp)
#for i in range(1, max(A)+1):
#    print(Z[i]*ipl%mod)