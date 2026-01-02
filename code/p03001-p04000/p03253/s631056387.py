def resolve():
    N,M = map(int,input().split())
    import sys
    def modinv(a, mod=10**9+7):
        return pow(a, mod-2, mod)
    def primes(m):
        temp = m
        a = []
        if temp % 2 == 0:
            a.append(1)
            temp //= 2
            while(temp % 2 == 0):
                a[0] += 1
                temp //= 2
        p = 3
        while(p*p < m):
            if temp % p == 0:
                a.append(1)
                temp //= p
                while(temp % p == 0):
                    a[-1] += 1
                    temp //= p
            p += 2
        if temp != 1:
            a.append(1)
        return a
    prime_list = primes(M)
    if prime_list == []:
        print(1)
        sys.exit()
    H = [0 for _ in range(max(prime_list)+1)]
    H[0] = 1
    for k in range(max(prime_list)):
        H[k+1] = (N+k) * H[k] * modinv(k+1) % int(1e9+7)
    ans = 1
    for pr in prime_list: 
        ans *= H[pr]
        ans %= int(1e9+7)
    print(ans)
resolve()