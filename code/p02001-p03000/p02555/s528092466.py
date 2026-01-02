def getval():
    s = int(input())
    return s


def main(s):
    #Combination calculation using mod m
    mod = 10**9+7
    lim = 10**5
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

    ans = 0
    for i in range(1,700):
        if 3*i>s:
            break
        n = s - 3*i
        temp = mod_comb(n+i-1,n)
        ans += temp 
        ans %= mod 

    print(ans)
        
    

if __name__=="__main__":
    s = getval()
    main(s)