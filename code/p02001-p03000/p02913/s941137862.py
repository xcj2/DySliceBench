def solve():
    N = int(input())
    S = input()

    base = 37
    def rolling_hash(s, mod):
        l = len(s)
        h = [0]*(l + 1)
        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        pw = [1]*(l + 1)
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
        return h, pw

    mod1 = 10**9 + 9; mod2 = 10**9 + 7
    h1, pw1 = rolling_hash(S, mod1)
    h2, pw2 = rolling_hash(S, mod2)

    def chk(l, h, pw, mod):
        p = pw[l]
        for i in range(min(l, N-2*l+1)):
            D[i] = (h[l+i] - h[i]*p) % mod
        s = set()
        for i in range(l, N-l+1):
            s.add(D[i-l])
            D[i] = v = (h[l+i] - h[i]*p) % mod
            if v in s:
                return 1
        return 0

    H = [set() for i in range(N//2+2)]
    D = [0]*N
    E = [0]*N
    k = N//2
    for l in range(1, N//2+1):
        if not chk(l, h1, pw1, mod1):
            k = l-1
            break
    ans = 0
    for l in range(k, 0, -1):
        if chk(l, h2, pw2, mod2):
            ans = l
            break
    print(ans)
solve()