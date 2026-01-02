def getval():
    n = int(input())
    return n 

def main(n):
    mod = 10**9+7
    #Number of comb for 1-8
    pow8 = [1]
    for i in range(n):
        temp = pow8[i] * 8
        temp %= mod 
        pow8.append(temp)

    #Number of comb for 0 and 9
    pow2 = [1]
    for i in range(n):
        temp = pow2[i] * 2
        temp %= mod
        pow2.append(temp)
    for i in range(n+1):
        temp = pow2[i] - 2
        if temp<=0:
            temp = 0
        pow2[i] = temp 

    ans = 0

    lim = n + 1
    fact = [1,1]
    inv = [1,1]
    finv = [1,1]
    for i in range(2,lim+1):
        fact.append((fact[i-1] * i) % mod)
        inv.append(mod - inv[mod%i] * (mod // i) % mod)
        finv.append(finv[i-1] * inv[i] % mod)
    def mod_comb(n,k):
        if n<k:
            return 0
        if n<0 or k<0:
            return 0
        return fact[n] * (finv[k] * finv[n-k] % mod) % mod

    for i in range(n+1):
        temp = pow2[i]*pow8[n-i]*mod_comb(n,i)
        temp %= mod
        ans += temp 
        ans %= mod

    print(ans)

if __name__=="__main__":
    n = getval()
    main(n)