def gcd(a,b):
    return gcd(b,a%b) if a%b else b

def break_primes(n):
    pn = n
    cnt = 0
    d = set()
    while pn % 2 == 0:
        pn //= 2
        d.add(2)
    p = 3
    while(p*p <= n):
        if pn % p == 0:
            d.add(p)
        while(pn % p == 0):
            pn //= p
        p += 2
    if pn != 1:
        d.add(pn)
    return d

def vectorize(n,primes,a):
    pn = n
    for p in range(len(primes)):
        a[p] = 0
        while pn % primes[p] == 0:
            a[p] += 1
            pn //= primes[p]


N = int(input())
A = list(map(int,input().split()))
if N == 2:
    print(max(A[0],A[1]))
if N > 2:
    primes = list(break_primes(gcd(A[0],A[1]))|break_primes(gcd(A[1],A[2]))|break_primes(gcd(A[2],A[0])))
    P = len(primes)
    vec_0 = [0 for _ in range(P)]
    vec_1 = [0 for _ in range(P)]
    vectorize(A[0],primes,vec_0)
    vectorize(A[1],primes,vec_1)
    perfect = [0 for _ in range(P)]
    perfect_idx = [ -1 for _ in range(P)]
    onemiss = [0 for _ in range(P)]
    for p in range(P):
        perfect_idx[p] = 0 if vec_0[p] < vec_1[p] else 1
        perfect[p] = min(vec_0[p],vec_1[p])
        onemiss[p] = max(vec_0[p],vec_1[p])
    vec_n = [0 for _ in range(P)]
    for n in range(2,N):
        vectorize(A[n],primes,vec_n)
        for p in range(P):
            if vec_n[p] < perfect[p]:
                onemiss[p] = perfect[p]
                perfect[p] = vec_n[p]
                perfect_idx[p] = n
            elif vec_n[p] < onemiss[p]:
                onemiss[p] = vec_n[p]
    import collections
    d = collections.defaultdict(lambda :1)
    ans = 1
    for p in range(P):
        ans *= primes[p] ** perfect[p]
        d[perfect_idx[p]] *= primes[p] ** (onemiss[p]-perfect[p])
    if len(d.items()) == 0:
        print(ans)
    else:
        print(ans*max(d.items(),key=lambda x:x[1])[1])