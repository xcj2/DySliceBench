def a():
    mod = 998244353
    o = [0] * 63

    def bi(x):
        i = 0
        while x != 0:
            o[i] = x%2
            x //= 2
            i += 1

    bi(mod-2)

    def modinv(m):
        b = 1
        p = m
        for i in range(63):
            if i:
                p = (p * p)%mod
            if o[i]:
                b *= p
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
