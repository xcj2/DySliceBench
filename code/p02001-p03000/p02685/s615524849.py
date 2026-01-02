def a():
    mod = 998244353

    def bi(x):
        o = []
        while x != 0:
            o.append(x%2)
            x //= 2
        return o

    o = bi(mod - 2)
    leo = len(o)
    p = [0] * leo

    def modinv(m):
        p[0] = m
        for i in range(1,leo):
            a = p[i-1]
            a *= a
            a %= mod
            p[i] = a
        b = 1
        for i in range(leo):
            if o[i]:
                b *= p[i]
                b %= mod
        return b

    N,M,K = map(int,input().split())

    C = [1]*(K+1)
    for i in range(1,K+1):
        C[i] = (C[i-1] * (N-i) * modinv(i))%mod

    M1 = [1]*N
    for i in range(1,N):
        M1[i] = M1[i-1] * (M-1)
        M1[i] %= mod

    ans = 0
    for k in range(0,K+1):
        ans += C[k] * M * M1[N-k-1]
        ans %= mod

    print(ans)

a()
