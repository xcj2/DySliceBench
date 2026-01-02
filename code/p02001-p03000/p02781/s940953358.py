def main():
    mod = 10**9+7
    fact = [1, 1]
    for i in range(2, 10**3):
        fact.append(fact[-1]*i % mod)

    def inv_n(n):
        return pow(n, mod-2, mod)

    def nCr(n, r, mod=10**9+7):
        return inv_n(fact[n-r]*fact[r] % mod)*fact[n] % mod

    n = input()
    k = int(input())

    m = len(n)
    ans2 = 0
    if len(n)-n.count("0") == k:
        ans2 = 1
    for i in range(m):
        s = n[i]
        if s != "0":
            if k >= 0 and m-i-1 >= k:
                ans2 += nCr(m-i-1, k)*pow(9, k)
            k -= 1
            if k >= 0 and m-i-1 >= k:
                ans2 += (int(n[i])-1)*nCr(m-i-1, k)*pow(9, k)
    print(ans2)


main()