def main():
    mod = 2**31-1
    pow3 = [1]*200001
    p = 1
    i3 = pow(3, mod-2, mod)
    for i in range(1, 200001):
        p = p*3 % mod
        pow3[i] = p

    def rolling_hash(seq):
        h = 0
        for i, j in enumerate(seq):
            h += (j+1)*pow3[i]
        h %= mod
        H0s = [0]*n
        for i, j in enumerate(seq):
            H0s[i] = h
            h = (h-j-1+(j+1)*pn)*i3 % mod
        return H0s

    def rolling_hash2(seq):
        p = 0
        p2 = 0
        for i, j in enumerate(seq):
            p += (j+1)*pow3[i]
            p2 += (2-j)*pow3[i]
        return p % mod, p2 % mod

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = max(a+b)
    a1 = [0]*n
    b1 = [0]*n
    memo = [0]*n
    cnt = n
    pn = pow3[n]

    for k in range(len(bin(m))-2):
        k2 = 2**k
        for i, j in enumerate(a):
            a1[i] = (j & k2) >> k
        for i, j in enumerate(b):
            b1[i] = (j & k2) >> k
        b_hash, b_hash2 = rolling_hash2(b1)
        A1 = rolling_hash(a1)
        for i, (j, k) in enumerate(zip(memo, A1)):
            if j is None:
                continue
            elif k == b_hash:
                pass
            elif k == b_hash2:
                memo[i] += k2
            else:
                memo[i] = None
                cnt -= 1
        if cnt == 0:
            return

    for i, j in enumerate(memo):
        if j is not None:
            print(i, j)


main()