def main():

    N, M = map(int, input().split())
    mod = pow(10, 9) + 7

    g1 = [1, 1]
    g2 = [1, 1]
    inv = [0, 1]

    for i in range(2, max(M, N)+1):
        g1.append((g1[-1] * i) % mod)
        inv.append( ( -inv[mod % i] * (mod//i)) % mod )
        g2.append((g2[-1] * inv[-1]) % mod)

    def combi(n, r):
      r = min(r, n-r)
      return g1[n]*g2[r]*g2[n-r]%mod

    def p(n, r):
      return g1[n]*g2[n-r]%mod

    if M < N: return 0

    ans = 0
    sgn = 1
    for i in range(N+1):
        v = sgn * combi(N, i) * p(M, i)
        v %= mod
        v *= p(M-i, N-i) * p(M-i, N-i)
        v %= mod
        ans += v
        ans %= mod
        sgn *= -1
    return ans



if __name__ == '__main__':
    print(main())