N,A,B = map(int,input().split())
def power_func(a,n,p=10**9+7):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %p
        if bi[i]=="1":
            res=(res*a) %p
    return res

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
#ans = power_func(2,N) - 1 - combination(N,A) - combination(N,B)
ans = power_func(2,N) - 1
ans = ans if ans >= 0 else ans + 10 ** 9 + 7
ans = ans - combination(N,A)
ans = ans if ans >= 0 else ans + 10 ** 9 + 7
ans = ans - combination(N,B)
ans = ans if ans >= 0 else ans + 10 ** 9 + 7
print(ans)